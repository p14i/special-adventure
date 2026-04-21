import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.header("Tweet Generator")
st.subheader("Generate Tweets with generative AI")

# Put your API key in environment variables before running:

os.environ['GOOGLE_API_KEY'] = "AIzaSyDsdkkMNAP1O-REa0QqMOrw2Zd0bl0x9S8"

tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(
    template=tweet_template,
    input_variables=["number", "topic"]
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

tweet_chain = tweet_prompt | llm | StrOutputParser()

topic = st.text_input("Topic")
number = st.number_input("Number of Tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate"):
    if topic.strip():
        tweets = tweet_chain.invoke({"number": number, "topic": topic})
        st.write(tweets)
    else:
        st.warning("Please enter a topic.")
