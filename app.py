
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit App
st.title("VADER Sentiment Analysis")

# Introduction
st.markdown(
    '''
    **What is VADER Sentiment Analysis?**

    VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool specifically designed for social media text.
    It detects the polarity (positive or negative) and intensity of sentiment in textual data.

    ### How It Works:
    - VADER uses a sentiment lexicon, a predefined list of sentiment-related words, to calculate sentiment scores.
    '''
)

# Input Text Area
text_input = st.text_area("Enter the text for sentiment analysis:", "")

if st.button("Analyze Sentiment"):
    if text_input.strip():
        # Analyze sentiment
        scores = analyzer.polarity_scores(text_input)
        st.subheader("Sentiment Scores")
        st.write(scores)

        # Visualization
        st.subheader("Sentiment Breakdown")
        st.bar_chart(
            {
                "Sentiment": ["Positive", "Neutral", "Negative", "Compound"],
                "Score": [scores["pos"], scores["neu"], scores["neg"], scores["compound"]],
            }
        )
    else:
        st.warning("Please enter some text to analyze.")

# Footer
st.markdown("**Powered by VADER Sentiment Analysis**")
