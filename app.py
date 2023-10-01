import nltk
nltk.download('vader_lexicon')

import os
from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None

    if request.method == 'POST':
        sentence = request.form['sentence']
        sentiment = analyze_sentiment(sentence)

    return render_template('index.html', sentiment=sentiment)

def analyze_sentiment(sentence):
    sentiment_scores = sia.polarity_scores(sentence)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

