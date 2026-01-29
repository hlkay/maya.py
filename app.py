import streamlit as st
import random
import time

HER_NAME = "Maya"

st.set_page_config(
    page_title="For my Bé iu",
    page_icon="❤️",
    layout="centered"
)

# ---------- STYLES ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff1f5, #fdfbfb);
}

.container {
    max-width: 600px;
    margin: auto;
    margin-top: 10vh;
    padding: 50px 40px;
    background: rgba(255,255,255,0.85);
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    text-align: center;
}

.title {
    font-size: 2.6rem;
    font-weight: 600;
    color: #3a3a3a;
    margin-bottom: 30px;
}

.message {
    font-size: 1.4rem;
    color: #444;
    margin-top: 30px;
    line-height: 1.6;
    animation: fadeIn 1.2s ease-in-out;
}

.final {
    font-size: 1.8rem;
    color: #2f2f2f;
    margin-top: 50px;
    line-height: 1.8;
    animation: fadeIn 2s ease-in-out;
}

button[kind="primary"] {
    background: #f4a7b9;
    border-radius: 999px;
    padding: 0.6em 1.6em;
    font-size: 1.1rem;
    border: none;
}

button[kind="primary"]:hover {
    background: #f191a8;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# ---------- CONTENT ----------
messages = [
    "You make my days feel lighter without even trying.",
    "Being with you feels calm, warm, and right.",
    "I notice the little things you do more than you know.",
    "Somehow, life makes more sense with you in it.",
    "I don’t say it enough, but I appreciate you deeply.",
]

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if "done" not in st.session_state:
    st.session_state.done = False

if "current_message" not in st.session_state:
    st.session_state.current_message = ""

st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="title">A little something for you</div>', unsafe_allow_html=True)

if not st.session_state.done:
    if st.button("Tap gently"):
        st.session_state.clicks += 1
        time.sleep(0.3)

        if st.session_state.clicks < 5:
            st.session_state.current_message = random.choice(messages)
        else:
            st.session_state.done = True

if not st.session_state.done and st.session_state.current_message:
    st.markdown(
        f'<div class="message">{st.session_state.current_message}</div>',
        unsafe_allow_html=True
    )

if st.session_state.done:
    st.markdown(
        f"""
        <div class="final">
            {HER_NAME},<br><br>
            I love you — quietly, deeply,<br>
            and more every day.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
