import time
import json
import requests
import streamlit as st
from record import *


def chat(msg_in):
    return {"role": "assistant", "content":f"{str(msg_in)}"}

def get_today():
    try :
        response_zh = requests.get("https://jkapi.com/api/wanan")
        response_en = requests.get(f"https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={response_zh.text}")
        parsed_data = json.loads(response_en.text)
        tgt_values = [item["tgt"] for item in parsed_data["translateResult"][0]]
        tgt_string = "".join(tgt_values)
        return tgt_string
    except:
        return "Good Night！"


if __name__ == '__main__':
    st.set_page_config(
    page_title="Record",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)
    

    with st.sidebar:
       pass

    
    if "msg_today" not in st.session_state:
        # st.session_state.msg_today = get_today()
        st.session_state.msg_today = 'Good Night!'
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]
    if "result_a" not in st.session_state:
        st.session_state.result_a = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]
    if "result_b" not in st.session_state:
        st.session_state.result_b = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]

    st.success(st.session_state.msg_today, icon="🌃")
    st.title("💬 Record")
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        lines = prompt.splitlines()
        for line in lines:
            st.chat_message("user").write(line)
            msg_get,result_get = RecordData(line).run()
            st.session_state.result_a = [item_y + item_x for item_x, item_y in zip(result_get[0],st.session_state.result_a)]
            st.session_state.result_b = [item_y + item_x for item_x, item_y in zip(result_get[1],st.session_state.result_b)]
            msg = chat(msg_get)
            # print(msg["content"])
            st.session_state.messages.append(msg)
            st.chat_message("assistant").text(str(msg["content"]))
            time.sleep(0.5)
