import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
page_title="Record",
page_icon="🤖",
layout="wide",
initial_sidebar_state="expanded",
)
with st.sidebar:
    pass

st.title("📊Result")

if "result_a" not in st.session_state:
    st.session_state.result_a = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]
if "result_b" not in st.session_state:
    st.session_state.result_b = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]
if "index_list" not in st.session_state:
    st.session_state.index_list = [i+1 for i in range(49)]

tab1, tab2 = st.tabs(["Macau", "HongKong"])

with tab1:
    result_a = [i[1:] for i in st.session_state.result_a]
    result_a = [sum(i) for i in result_a]

    plt.pie(result_a)
    plt.title("Pie Chart for Macau")
    st.pyplot(plt.gcf())

with tab2:
    st.dataframe(pd.DataFrame(st.session_state.result_b, index=st.session_state.index_list))


# Add a button to scroll to the bottom of the page
if st.button("Scroll to Bottom"):
    # This is a JavaScript code snippet to scroll to the bottom
    st.write('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)
