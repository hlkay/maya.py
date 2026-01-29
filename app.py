import streamlit as st

HER_NAME = "Bé iu"

st.set_page_config(
    page_title="For You",
    page_icon="💗",
    layout="centered"
)

st.markdown("""
<style>
body {
    background-color: #fff7fb;
}

.container {
    text-align: center;
    margin-top: 12vh;
}

.heart {
    font-size: 5rem;
    transition: all 0.3s ease;
}

.text {
    font-size: 1.4rem;
    margin-top: 20px;
    color: #444;
}

.final {
    font-size: 1.6rem;
    margin-top: 30px;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

steps = [
    ("🤍", "Tap it."),
    ("💗", "Okay… again."),
    ("💖", "It’s growingggg."),
    ("💞", "Just a little bit moreee hehe."),
    ("❤️", "Yayyyy you got itt."),
]

if "step" not in st.session_state:
    st.session_state.step = 0

st.markdown('<div class="container">', unsafe_allow_html=True)

if st.session_state.step < len(steps):
    heart, text = steps[st.session_state.step]

    st.markdown(f'<div class="heart">{heart}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{text}</div>', unsafe_allow_html=True)

    if st.button("Tap"):
        st.session_state.step += 1
else:
    st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="final">
            Hello my {HER_NAME}.<br><br>
            I just wanted to make something small<br>
            to remind you that I love you so much.
        </div>
        """,
        unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

