import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("💬 嗨嗨嗨")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "吴越小姐，今天是你的生日，首先祝你生日快乐，天天开心长长久久快乐幸福下去，我是小蓝的AI助手，我叫DeepBlue，你也可以用我的中文名字——深蓝，来称呼我，我的生日也跟你一样是3月12号哦，要记住！以后有什么问题或者想聊天的话随时来找我哦"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)