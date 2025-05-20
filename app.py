import streamlit as st
import json
import random

# 使用 Streamlit 缓存装饰器来避免重复加载文件
@st.cache_data
def load_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="题库小测试", layout="centered")
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📘党课题库</h1>", unsafe_allow_html=True)
    st.markdown("---")

    questions = load_questions()
    if not questions:
        st.error("❗ 没有加载到题目")
        return

    # 初始化随机题目索引
    if "q_idx" not in st.session_state:
        st.session_state.q_idx = random.randint(0, len(questions) - 1)

    question = questions[st.session_state.q_idx]

    # 显示题干
    st.markdown(
        f"""
        <div style='padding: 1em;
                    background-color: red;
                    border-radius: 10px;
                    font-size: 18px;
                    font-weight: bold;'>
            📝 <strong>题目：</strong> {question['question']}
        </div>
        """, unsafe_allow_html=True
    )

    # 显示选项
    selected = st.radio("🔘 请选择你的答案：", question["options"], key=question["id"])

    # 提交答案按钮
    if st.button("✅ 提交答案"):
        if selected == question["answer"]:
            st.success("🎉 回答正确！")
        else:
            st.error("❌ 回答错误")
        st.info(f"📌 正确答案是：**{question['answer']}**")

    # 换题按钮
    if st.button("🔄 换一道题"):
        st.session_state.q_idx = random.randint(0, len(questions) - 1)
        st.rerun()

    st.markdown("---")
    st.caption("© 2025 我的刷题助手 | Streamlit 构建")

if __name__ == "__main__":
    main()
