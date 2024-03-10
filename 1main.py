from flask import Flask, render_template, request,abort
import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
import requests
from bs4 import BeautifulSoup
import re
import json
import psycopg2
from wordcloud import WordCloud
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import matplotlib.pyplot as plt 
from io import BytesIO
import base64  
import os
from raw_data import list_data

politics_keywords,sports_keywords,technology_keywords,entertainment_keywords,health_keywords,education_keywords,financial_keywords,crime_keywords,science_keywords,stock_market_keywords,environment_keywords = list_data()

app = Flask(__name__)

# Text extractor
def extract_txt():
    try:
        url = request.form["URL"]
        
        if "indiatimes.com" in url:
            page = requests.get(url)
            soup = BeautifulSoup(page.content,"html.parser")
            
        
            parent_div = soup.find(class_="_s30J clearfix")

            text_py = parent_div.get_text() 
            txt_py = re.sub(r'[^\w\s\.]','',text_py)
            currency_pattern = r'[$€£¥₹]|\bUSD\b|\bEUR\b|\bGBP\b|\bJPY\b|\bINR\b|\bRs\b|\d'
            clean_text = re.sub(currency_pattern, '', txt_py)
            clean_txt_py = re.sub(r'[\.]','. ',txt_py)
        else:
            abort(406)
        return url,text_py,clean_text
    except:
        abort(406)

 

# Text analyzer..
def text_analysis(text_py,clean_txt_py):
    word_num_py = 0
    stp_words_num_py = 0
    sent_num_py = 0
    noun_py = 0
    pronoun_py = 0
    verb_py = 0
    adverb_py =0 
    adjective_py = 0
    pos_dict ={}
    
    # Words and sentences tokenisation
    word_lst = word_tokenize(clean_txt_py)
    sent_lst = sent_tokenize(text_py)
    sent_num_py = len(sent_lst)
    clean_txt = re.sub(r'[^\w\s]','',clean_txt_py)
    
    # Text without stopwords 
    lst_stp_words = nltk.corpus.stopwords.words("english")
    p = [word for word in word_tokenize(clean_txt) if word.lower() not in lst_stp_words]
    pure_txt = ' '.join(p)
    
    # All necessary information like: Total words,Total sentence, count of each stop words.
    
    punc_lst = [',','.','?','!']
    for i in word_lst:
        if i not in punc_lst:
            word_num_py += 1
        if i in lst_stp_words:
            stp_words_num_py += 1
    lst_pos = nltk.pos_tag(word_lst,tagset = "universal")
            
    pos_dict["Noun"] = 0
    pos_dict["Pronoun"] = 0
    pos_dict["Verb"] = 0
    pos_dict["Adverb"] = 0
    pos_dict["Adjective"] = 0
    for i in lst_pos:
        if i[1] == 'NOUN':
            pos_dict["Noun"] += 1
        elif i[1] == 'PRON':
            pos_dict["Pronoun"] += 1
        elif i[1] == 'VERB':
            pos_dict["Verb"] +=1
        elif i[1] == 'ADV':
            pos_dict["Adverb"] += 1
        elif i[1] =='ADJ':
            pos_dict["Adjective"] += 1
    
    return pure_txt,word_num_py,sent_num_py,pos_dict,lst_pos


# Function to predict the news genre based on the presence of keywords
def predict_news_genre(article_text):
    # Convert article text to lowercase for case-insensitive matching
    article_text_lower = article_text.lower()
    
    # Count the occurrences of keywords in the article text for each genre
    genre_counts = {
        "Politics": sum(keyword in article_text_lower for keyword in politics_keywords),
        "Sports": sum(keyword in article_text_lower for keyword in sports_keywords),
        "Technology": sum(keyword in article_text_lower for keyword in technology_keywords),
        "Entertainment": sum(keyword in article_text_lower for keyword in entertainment_keywords),
        "Health": sum(keyword in article_text_lower for keyword in health_keywords),
        "Education": sum(keyword in article_text_lower for keyword in education_keywords),
        "Financial": sum(keyword in article_text_lower for keyword in financial_keywords),
        "Crime": sum(keyword in article_text_lower for keyword in crime_keywords),
        "Science": sum(keyword in article_text_lower for keyword in science_keywords),
        "Stock Market": sum(keyword in article_text_lower for keyword in stock_market_keywords)
    }
    
    # Predict the genre based on the genre with the highest keyword count
    predicted_genre = max(genre_counts, key=genre_counts.get)
    
    return predicted_genre



# Text summrizer..
def Text_summary(text):
    num_sentences=7
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    summary =" ".join(str(sentence) for sentence in summary)
    return summary
# Reading time of the summary and article..
def read_time(text_py):
    rs1 = 170
    rs2 = 240
    wrd_lst = nltk.word_tokenize(text_py)
    read_time1 = len(wrd_lst)/rs1
    read_time2 = len(wrd_lst)/rs2
    return read_time1,read_time2

def freq_words(clean_txt_py,lst_pos): 
    txt_lst = nltk.word_tokenize(clean_txt_py)
    stp_word = (nltk.corpus.stopwords.words("english"))
    lst = [w.lower() for w in txt_lst if w not in  stp_word]
    refine_w = [w[0] for w in lst_pos if w[1] not in ('ADP','ADV','VERB')]
    fd = nltk.FreqDist([w.lower() for w in refine_w if w.lower() not in stp_word])
    # Sorting the dictionary by values in descending order
    sorted_dict_desc = dict(sorted(fd.items(), key=lambda item: item[1], reverse=True))
    re_dict = {}
    for key,value in sorted_dict_desc.items():
        if len(re_dict) <=8:
            re_dict[key] = value
    return re_dict

conn = psycopg2.connect(host = "localhost", database = "dhp2024", user = "postgres", password = "Saurabh@1")
cur = conn.cursor()

app.secret_key =os.urandom(24)

@app.route("/",methods=('POST','GET'))
def complier():
    text_py = ''
    clean_text = ''
    word_num_py = 0
    sent_num_py = 0
    stp_words_num_py = 0
    pure_txt = ''
    text_summary = ''
    pos_dict = {}
    wordcloud_image = None
    genere = ''
    
    if request.method =='POST':
        
        # url = request.form["URL"]
        keywords = {}
        url,text_py,clean_text = extract_txt()
        pure_txt,word_num_py,sent_num_py,pos_dict,lst_pos= text_analysis(text_py,clean_text)
        text_summary = Text_summary(text_py)
        genere = predict_news_genre(pure_txt)
        keywords = freq_words(clean_text,lst_pos)
        a,b = read_time(text_py)
        wordcloud = WordCloud(width=800, height=400, background_color='rgb(239,240,220)').generate_from_frequencies(keywords)

        # Save word cloud image to a file-like object
        wordcloud_image = BytesIO()
        wordcloud.to_image().save(wordcloud_image, format='PNG')
        wordcloud_image.seek(0)

        
        wordcloud_image_encoded = base64.b64encode(wordcloud_image.getvalue()).decode('utf-8')
        try:
            cur.execute("insert into user_info(URL,words_count,sentence_count,pos_dict,text) values (%s,%s,%s,%s,%s)",(url,word_num_py,sent_num_py,json.dumps(pos_dict),text_py))
            conn.commit()
        except:
            pass
        
    
        return render_template("front.html", text_html=text_py,total_words_html=word_num_py, total_sent_html=sent_num_py, pos_html=pos_dict,summary_html=text_summary, wordcloud_image=wordcloud_image_encoded,genere_html = genere,t1=int(a),t2=int(b))
    return render_template("front.html", text_html='',total_words_html=0,
                        total_sent_html=0, pos_html={}, summary_html='', wordcloud_image='')


@app.route("/ViewDetails",methods=('POST','GET'))
def Viewdetails():
    data_py = []
    conn = psycopg2.connect(
    host = "localhost", database = "dhp2024", user = "postgres", password = "Saurabh@1")
    cur = conn.cursor() 
    if request.method == 'POST':
        if request.form['password'] == "sitare@1":
            cur.execute("select * from user_info")
            data = cur.fetchall()
            data_py = data
            conn.commit()
            return render_template("user_detail.html", data_html = data_py)
        else:
            return abort(401)
@app.route("/login",methods=('POST','GET'))
def login():
    return render_template("back.html")
if __name__ == "__main__":
    app.run(debug = True)
