import streamlit as st
import random

# --- CONFIG ---
HER_NAME = "Maya"   # ← change this

st.set_page_config(
    page_title="For my Bé iu",
    page_icon="❤️",
    layout="centered"
)

# --- STYLES ---
st.markdown("""
<style>
.big-title {
    text-align: center;
    font-size: 3rem;
    color: #e75480;
}
.message {
    text-align: center;
    font-size: 1.6rem;
    margin-top: 20px;
}
.final {
    text-align: center;
    font-size: 2.2rem;
    color: #ff1493;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<div class="big-title">A Little Surprise</div>', unsafe_allow_html=True)

messages = [
    "You make my heart smile every single day",
    "Life feels magical with you in it",
    "I’m so lucky to have you",
    "You’re my favorite notification",
    "Every moment with you is my favorite",
    "You’re the best thing that ever happened to me",
]

# --- STATE ---
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if "done" not in st.session_state:
    st.session_state.done = False

# --- BUTTON LOGIC ---
if not st.session_state.done:
    if st.button("💌 Tap here"):
        st.session_state.clicks += 1

        if st.session_state.clicks < 5:
            st.markdown(
                f'<div class="message">{random.choice(messages)}</div>',
                unsafe_allow_html=True
            )
        else:
            st.session_state.done = True

# --- FINAL MESSAGE (STAYS FOREVER) ---
if st.session_state.done:
    st.markdown(
        f"""
        <div class="final">
            {HER_NAME},<br><br>
            I love you so much<br>
        </div>
        """,
        unsafe_allow_html=True
    )
