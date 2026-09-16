import streamlit as st
import preprocessor

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    st.write("File uploaded successfully")
    st.write("Characters:", len(data))

    df = preprocessor.preprocess(data)

    st.write("Shape:", df.shape)
    st.write(df.head())

    # fetch unique users
    user_list = df['user'].unique().tolist()

    st.sidebar.selectbox("Show analysis wrt",user_list)