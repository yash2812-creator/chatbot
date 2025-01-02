from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

# Thired party integration using langchain_community 
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()

#langchian tracking
os.environ['LANGCHAIN_TRACKING'] ="true"
#os.environ['LANGCHAIN_API_KEY'] =os.getenv("LANGCHAIN_API_KEY")

# Define the LLM model
promt = ChatPromptTemplate([
    ("system","your personalized assitant. Please respond to user requests"),
    ("user","Questions:{question}")

])

#streamlit framework
st.title("langchain Demo with ollama")
input_text =st.text_input("Ask anything...")

#llm model
llm = Ollama(model="LLAMA2")
ouput_parser = StrOutputParser()
chain = promt|llm|ouput_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))
    