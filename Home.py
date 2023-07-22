import streamlit as st
import streamlit.components.v1 as components


OpenAI_Key = st.secrets["OPENAI_KEY"]

st.set_page_config(
    page_title="EduQuest",
    page_icon="https://cdn-icons-png.flaticon.com/512/2617/2617909.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.image("images/eduquest-logo2.png", width= 400)

st.markdown("""
#### Welcome to EduQuest - a 5 in 1 education multitool for students.
            
**Text Summarizer**: Use our Text Summarizer to efficiently generate concise summaries from PDFs, articles, or input text. Save time and get the main points without reading lengthy content.
 
**Video Summarizer**: With the Video Summarizer, simply paste a YouTube video URL, and we'll provide you with a summary that includes the essential keywords used. No need to watch the entire video to grasp its content.
 
**Semantic Search**: Upload a text file and benefit from our advanced Semantic Search feature. Easily find relevant information based on keywords, making research faster and more efficient.
            
**Notes and Questions** : Input any topic, and our tool will generate comprehensive notes or questions related to that subject. Enhance your learning experience with organized and structured content.

**Chatbot** : Interact with our Chatbot by uploading .CSV or .TXT files, perfect for Zoom transcripts. Engage in natural conversations and obtain quick answers to your queries.
""")
 