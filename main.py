# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
st.title('인공지능 글작가')
content = st.text_input('글의 주제를 제시해주세요.')
if st.button('글 작성 요청하기.'):
    with st.spinner('글 작성 중...'):
        result = chat_model.predict(content + '에 대한 글을 써줘')
        st.write(result)