from codecs import ignore_errors
import streamlit as st
import pandas as pd
from io import StringIO

st.write('''
DigiparkのCSVをどうぞ
''')
         
import os
OPENAI_KEY = os.environ.get('OPENAI_KEY')
assert OPENAI_KEY, "key where?"

label='csv'
uploaded_file = st.file_uploader(label, type=['.csv'], accept_multiple_files=False)

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    print(bytes_data)
    string_data = bytes_data.decode("utf-8")
    # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO()
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
else:
    st.write('no file')