def list_data():
    # Politics Keywords List
    politics_keywords = [
        "politics", "government", "election", "policy", "president", "congress", "parliament", "vote",
        "political", "legislation", "diplomacy", "constitution", "political party",
         "governance",  "international relations", "foreign policy",  "judiciary",
        "political theory", "political science", "political ideology", "political philosophy", 
          "legislativ", "administration",  "corruption", "transparency", "accountability",
        "dictatorship",  "federalism",  "public service",
        "political leader", "political movement", "civil liberties", "human rights", "citizenship", "nationalism", "globalism",
        "populism", "fascism", "communism", "socialism", "anarchy", "capitalism", "social democracy", "neoliberalism", "conservatism",
        "liberalism",  "activism", "protest", "revolution", "secession", "national security",
        "public opinion", "political culture", "political identity", "political behavior", "voter turnout", "electoral system", "political economy",
        "political psychology", "political sociology"
    ]

    # Sports Keywords List
    sports_keywords= [
        "sports", "football", "basketball", "soccer", "tennis", "athlete", "game", "tournament", "match", "championship",
        "team", "league", "score", "goal", "player", "coach", "referee", "stadium", "arena", "ball", "field", "court",
        "pitch", "track", "competition", "event", "medal", "trophy", "record", "training", "practice", "fitness", "exercise",
        "workout", "gym", "conditioning", "warm-up", "stretching", "strength", "endurance", "speed", "agility", "flexibility",
        "technique", "strategy", "tactics", "playbook", "offense", "defense"
    ]
    # Technology Keywords List
    technology_keywords= [
        "technology", "innovation", "internet", "software", "startup", "digital", "AI", "artificial intelligence", "tech",
        "algorithm", "coding", "programming", "hardware", "computer", "device", "smartphone", "tablet", "laptop", "desktop",
        "operating system", "app", "application", "website", "web development", "mobile app", "cloud computing", "data", "big data",
        "data analysis", "data science", "machine learning", "deep learning", "neural network", "automation", "robotics", "internet of things",
        "IoT", "virtual reality", "VR", "augmented reality", "AR", "wearable technology", "smartwatch", "fitness tracker", "biotechnology",
        "genetic engineering", "DNA sequencing", "bioinformatics", "nanotechnology", "quantum computing", "cybersecurity", "encryption",
        "network security", "privacy", "digital rights", "intellectual property", "patent", "copyright", "trademark", "open source",
        "software development", "agile", "scrum", "DevOps", "version control", "git", "GitHub", "collaboration", "communication",
        "social media", "networking", "wireless", "5G", "broadband", "satellite", "telecommunication"
    ]

    # Entertainment Keywords List
    entertainment_keywords= [
        "entertainment", "celebrity", "movie", "music", "TV", "Hollywood", "showbiz", "film", "entertain", "star",
         "award", "actor", "actress", "director", "producer", "screenplay", "script", "plot", "character",
        "cast", "crew", "set", "stage", "scene", "special effects", "CGI", "animation", "motion capture",
        "visual effects", "soundtrack", "score", "theme", "genre", "drama", "comedy", "romance", "action", "adventure",
        "fantasy", "science fiction", "horror", "thriller", "mystery", "suspense",  
        "noir", "western", "war",  "biographical",  "documentary", "reality TV", 
        "variety show", "game show",  "soap opera", "cartoon", "anime", "manga", "web series", "streaming",
        "binge-watching", "blockbuster", "box office", "gross", "revenue", "profit", "release", "premiere", "opening", "closing",
        "review", "critique", "rating", "festival", "red carpet", "scandal"]
    # Health Keywords List
    health_keywords = ["health", "wellness", "medicine", "doctor", "fitness", "nutrition", "medical", "wellbeing", "hospital", "diagnosis",
        "treatment", "disease", "mental health", "physical health", "emotional health", "holistic health", "preventive care",
        "primary care", "specialist", "surgery", "therapy", "counseling", "rehabilitation", "recovery", "chronic", "acute",
        "terminal", "disability", "condition", "illness", "infection", "virus", "bacteria", "immune system", "vaccination",
        "immunization", "public health", "epidemiology", "outbreak", "pandemic", "epidemic", "contagion", "quarantine", "isolation",
        "hygiene", "cleanliness", "sanitation", "hydration", "sleep", "rest", "relaxation", "stress", "anxiety", "depression",
        "addiction", "substance abuse", "alcoholism", "drug abuse", "smoking", "tobacco", "caffeine", "diet", "calorie"]


    # Educational Keywords
    education_keywords = [
        "school", "university", "college", "student", "learning", "teacher", "classroom", "academic", "degree", "study",
        "curriculum", "educational", "research", "books", "knowledge", "lesson", "exam", "homework", "assignment", "lecture",
        "tutor", "professor", "graduation", "diploma", "scholarship", "seminar", "workshop", "laboratory", "experiment", "science",
        "math", "physics", "chemistry", "biology", "history", "geography", "literature", "arts", "music", "language",
        "computer", "programming", "engineering", "architecture", "medicine", "law", "business", "economics", "philosophy", "psychology",
        "sociology", "anthropology", "archeology", "astronomy", "botany", "geology", "paleontology", "zoology", "ecology", "ethics",
        "morality", "critical thinking", "problem-solving", "creativity", "innovation", "analysis", "experimentation", "observation", "hypothesis",
        "conclusion", "thesis", "dissertation", "peer review", "academic journal", "citation", "reference", "plagiarism", "diversity",
        "inclusion", "equality", "access", "equity", "quality", "standardized testing", "assessment", "evaluation", "accreditation", "accredited",
        "certification", "continuing education", "lifelong learning", "online learning", "distance education", "vocational training", "skill development",
        "professional development", "career advancement", "research", "analysis", "experimentation"
    ]

    # Finance Keywords
    financial_keywords = [
        "finance", "economy", "business", "market", "investment", "money", "bank", "economic", "stock", "capital",
        "entrepreneur", "wealth", "financial", "transaction", "asset", "liability", "income", "revenue", "profit",
        "loss", "budget", "debt", "credit", "loan", "mortgage", "interest", "rate", "currency", "exchange",
        "foreign exchange", "inflation", "deflation", "recession", "depression", "boom", "bust", "fiscal", "monetary",
        "policy", "regulation", "tax", "taxation", "revenue", "expenditure", "public finance", "private finance", "personal finance",
        "corporate finance", "government finance", "central bank", "federal reserve", "interest rate", "bond",  "equity", "dividend", "mutual fund", "hedge fund", "pension", "retirement", "insurance",
        "risk", "portfolio", "asset allocation", "diversification", "derivative", "option", "futures", "forward", "swap",
        "credit default swap", "securitization", "mortgage-backed security", "financial institution", "bankruptcy", "merger", "acquisition", "initial public offering",
        "venture capital", "angel investor", "crowdfunding", "cryptocurrency", "blockchain", "bitcoin", "ethereum", "regulation", "compliance",
        "anti-money laundering", "know your customer", "financial statement", "accounting", "auditor", "financial reporting", "audit", "financial planning",
        "investment banking", "commercial banking", "corporate governance"
    ]

    # Crime Keywords
    crime_keywords = [
        "crime", "police", "criminal", "investigation", "law", "officer", "justice", "criminality", "felony", "burglary",
        "robbery", "murder", "theft", "arrest", "court", "evidence", "suspect", "defendant", "accused",
        "trial", "verdict", "sentence", "prison", "jail", "correctional", "conviction", "guilty", "innocent",
        "witness", "testimony", "alibi", "forensic", "crime scene", "DNA", "fingerprint", "weapon", "motive",
        "opportunity", "modus operandi", "criminal law", "civil law", "legal system", "judiciary", "jurisdiction",
        "prosecutor", "defense attorney", "public defender", "plea bargain", "grand jury", "indictment", "appeal", "homicide",
        "assault", "battery", "rape", "kidnapping", "child abuse", "domestic violence", "cybercrime", "identity theft",
        "fraud", "white-collar crime", "embezzlement", "bribery", "corruption", "money laundering", "drug trafficking", "smuggling",
        "terrorism", "extortion", "racketeering", "organized crime", "gang", "mafia", "cartel", "narcotics", "narcotic",
        "narcotics trafficking", "drug cartel", "drug lord", "kingpin", "gang violence", "juvenile delinquency", "probation",
        "parole", "rehabilitation", "reentry", "recidivism", "crime prevention", "community policing", "neighborhood watch", "victim",
        "victimization", "restitution", "compensation", "legal aid"
    ]

    # Science Keywords
    science_keywords = [
        "science", "research", "scientist", "discovery", "experiment", "biology", "physics", "chemistry", "astronomy", "scientific",
        "laboratory", "innovation", "hypothesis", "theory", "experimentation", "observation", "data", "analysis", "conclusion",
        "methodology", "variables", "control", "independent variable", "dependent variable", "population", "sample", "survey",
        "questionnaire", "data collection", "data analysis", "science", "math", "physics", "chemistry", "biology", "history",
        "geography", "literature", "arts", "music", "language", "computer", "programming", "engineering", "architecture", "medicine",
        "law", "business", "economics", "philosophy", "psychology", "sociology", "anthropology", "archeology", "astronomy",
        "botany", "geology", "paleontology", "zoology", "ecology", "ethics", "morality", "critical thinking", "problem-solving",
        "creativity", "innovation", "research", "analysis", "experimentation", "observation", "hypothesis", "conclusion", "thesis",
        "dissertation", "peer review", "academic journal", "citation", "reference", "plagiarism"
    ]

    # Stock Market Keywords
    stock_market_keywords = [
        "stock market", "stocks", "trading", "investment", "NYSE", "NASDAQ", "shares", "investor", "stock exchange", "portfolio",
        "dividend", "bull market", "bear market", "day trading", "financial", "finance", "economy", "business", "market",
        "investment", "money", "bank", "economic", "stock", "capital", "entrepreneur", "wealth", "financial", "transaction",
        "asset", "liability", "income", "revenue", "profit", "loss", "budget", "debt", "credit", "loan",
        "mortgage", "interest", "rate", "currency", "exchange", "foreign exchange", "inflation", "deflation", "recession",
        "depression", "boom", "bust", "fiscal", "monetary", "policy", "regulation", "tax", "taxation",
        "revenue", "expenditure", "public finance", "private finance", "personal finance", "corporate finance", "government finance", "central bank",
        "federal reserve", "interest rate", "bond", "share", "equity", "dividend", "mutual fund", "hedge fund",
        "pension", "retirement", "insurance", "risk", "portfolio", "asset allocation", "diversification", "derivative",
        "option", "futures", "forward", "swap", "credit default swap", "securitization", "mortgage-backed security", "financial institution",
        "bankruptcy", "merger", "acquisition", "initial public offering", "venture capital", "angel investor", "crowdfunding", "cryptocurrency",
        "blockchain", "bitcoin", "ethereum", "regulation", "compliance", "anti-money laundering", "know your customer", "financial statement",
        "accounting", "auditor", "financial reporting", "audit", "financial planning", "investment banking", "commercial banking", "corporate governance"
    ]
    # Envirenmet_keywords
    environment_keywords = ["climate","change","global","warming","renewable","energy","sustainable","greenhouse","gases","carbon","footprint","biodiversity","deforestation","pollution","ecosystem","wildlife","conservation","resources","development","impact","action","emissions","effect","ecology","degradation","endangered","species","recycling","agriculture","awareness","control","disasters","air","water","efficiency","initiatives","offset","economy"]
    
    return politics_keywords,sports_keywords,technology_keywords,entertainment_keywords,health_keywords,education_keywords,financial_keywords,crime_keywords,science_keywords,stock_market_keywords,environment_keywords