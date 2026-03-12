# AI Electronics Purchase Advisor

An AI-powered recommendation system that helps customers choose the best electronics based on budget, usage, and product specifications.

## Problem

Many customers enter electronics stores without knowing which product best fits their needs.

This leads to:
- poor purchase decisions
- product returns
- longer sales cycles

## Solution

This project builds an intelligent product recommendation system that analyzes product datasets and recommends the best alternatives.

## Features

- AI-powered product recommendation
- Product comparison tool
- Budget-based filtering
- Market insights
- Interactive Streamlit interface

## Tech Stack

Python  
Streamlit  
Pandas  
Scikit-learn  
Kaggle datasets

## Project Structure

```
AI-Electronics-Purchase-Advisor
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── datasets
│   ├── cameras.csv
│   ├── laptops.csv
│   ├── phones.csv
│
├── models
│   ├── recommender.py
│   ├── comparison.py
│
├── notebooks
│   ├── EDA.ipynb
│
├── reports
│   ├── project_report.md
│
└── images
    ├── app_demo.png


```

## Requirements.txt

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
python-dotenv

```


## Running the Application

Clone repository
```
git clone https://github.com/Dhe-Reigner/AI-Electronics-Purchase-Advisor.git
```

Install dependencies
```
pip install -r requirements.txt
```

Run the app
```
streamlit run app.py
```

Example Use Case

```
Customer wants:

- Camera
- Budget: $800
- Use: YouTube

System recommends:

- Sony A6400
- Canon M50
- Fujifilm XT30

## Future Improvements

- Deep learning recommender
- review sentiment analysis
- price prediction model
- conversational AI assistant

## Author

Martin Kagema

Data Analyst | AI Engineer
```
