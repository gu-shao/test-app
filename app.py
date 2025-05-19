import streamlit as st
import json

# 加载题库
def load_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="练题系统", layout="centered")
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📘党课习题</h1>", unsafe_allow_html=True)
    st.markdown("---")

    questions = load_questions()
    total_questions = len(questions)
    if total_questions == 0:
        st.error("❗ 没有题目可用")
        return

    # 初始化当前题目索引（从 0 开始）
    if "q_idx" not in st.session_state:
        st.session_state.q_idx = 0

    question = questions[st.session_state.q_idx]
    st.markdown(
        f"""
        <div style='padding: 1em;
                    background-color: #ffccdd;
                    border-radius: 10px;
                    font-size: 18px;
                    font-weight: bold;'>
            📝 <strong>题目 {question['id']} / {total_questions}：</strong> {question['question']}
        </div>
        """, unsafe_allow_html=True
    )

    selected = st.radio("🔘 请选择你的答案：", question["options"], key=f"q_{question['id']}")

    if st.button("✅ 提交答案"):
        if selected == question["answer"]:
            st.success("🎉 回答正确！")
        else:
            st.error("❌ 回答错误")
        st.info(f"📌 正确答案是：**{question['answer']}**")

    # 下一题逻辑
    if st.button("➡ 下一题"):
        if st.session_state.q_idx < total_questions - 1:
            st.session_state.q_idx += 1
        else:
            st.info("🎉 已完成全部题目！")

    st.markdown("---")
    st.caption("© 2025 我的刷题助手 | 顺序刷题模式")

if __name__ == "__main__":
    main()
