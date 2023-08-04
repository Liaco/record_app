import time
import streamlit as st



def chat(msg_in):
    return {"role": "assistant", "content":f"{str(msg_in)}"}

if __name__ == '__main__':
    with st.sidebar:
       pass

    st.title("💬 Record")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]
    if "result_a" not in st.session_state:
        st.session_state.result_a = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]
    if "result_b" not in st.session_state:
        st.session_state.result_b = [["兔"], ["虎"], ["牛"], ["鼠"], ["猪"], ["狗"], ["鸡"], ["猴"], ["羊"], ["马"], ["蛇"], ["龙"]] * 4 + [['兔']]

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
            print(msg["content"])
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(str(msg["content"]))
            time.sleep(0.5)
