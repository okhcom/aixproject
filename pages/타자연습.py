import streamlit as st
import pandas as pd
import streamlit.components.v1 as htmlviewer

st.set_page_config(layout="wide")  # 전체 화면 사용 설정 (중요!)


# 🔹 HTML을 먼저 전체 너비로 출력
with open('./htmls/typing.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
    f.close()

htmlviewer.html(html1, height=800, scrolling=True)