import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./data/mydata.csv')

#global variable
url='https://youtu.be/XyEOEBsa8I4?si=zK2nf85_zWQKPk66'

#dictionaty
#ulrs = {
#    '윤리' [],
#    '코딩' []
#}
st.title('This is my fist webapp!!')
col1,col2 = st.columns((4,1))
with col1:
    with st.expander('SubContent1...'):
        st.subheader('SubContent1...')
        st.video(url)

    with st.expander('SubContent2...'):
        st.subheader('Image Content...')
        st.image('./images/dog.jpeg')

    with st.expander('SubContent3...'):
        st.subheader('Html Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html','r',encoding='utf-8') as f:
            html1=f.read()
            f.close()
        htmlviewer.html(html1,height=800,scrolling=True)

    with st.expander('SubContent...'):
        st.subheader('data App Content...')
        st.table(df)
        st.write(df.describe())
        fig, ax = plt.subplots(figsize=(20,10))
        df.plot(ax=ax)
        plt.savefig('./images/mygraph.png')
        st.image('./images/mygraph.png')



with col2:
    with st.expander('Tips....') :
        st.info('Tips...')