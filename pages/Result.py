import streamlit as st
import pandas as pd

with st.sidebar:
    pass

st.title("📑 Result")
if "result_a" not in st.session_state:
    st.session_state.result_a =  [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]
if "result_b" not in st.session_state:
    st.session_state.result_b = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]
if "index_list" not in st.session_state:
    st.session_state.index_list = [i+1 for i in range(49)]

tab1, tab2 = st.tabs(["Macau", "HongKong"])
with tab1:
    st.dataframe(pd.DataFrame(st.session_state.result_a,index=st.session_state.index_list))
with tab2:
    st.dataframe(pd.DataFrame(st.session_state.result_b,index=st.session_state.index_list))