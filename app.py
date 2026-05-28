import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #1e3c72, #2a5298);
    color: white;
}

/* Hide Streamlit Header/Footer */
header, footer {
    visibility: hidden;
}

/* Main Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #dcdcdc;
    margin-bottom: 30px;
    font-size: 18px;
}

/* User Chat Bubble */
.user-msg {
    background-color: #0084ff;
    color: white;
    padding: 12px 18px;
    border-radius: 18px;
    margin: 10px 0;
    margin-left: 80px;
    text-align: left;
    font-size: 16px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
}

/* Bot Chat Bubble */
.bot-msg {
    background-color: #ffffff;
    color: black;
    padding: 12px 18px;
    border-radius: 18px;
    margin: 10px 0;
    margin-right: 80px;
    text-align: left;
    font-size: 16px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
}

/* Chat Input */
.stChatInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 20px !important;
}

/* Mobile Responsive */
@media (max-width: 768px) {

    .user-msg {
        margin-left: 20px;
    }

    .bot-msg {
        margin-right: 20px;
    }

    .title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="title">🤖 AI FAQ Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask programming and AI related questions</div>',
    unsafe_allow_html=True
)

# ---------------- FAQ DATA ----------------

faq = {

    "python": "Python is a powerful and easy-to-learn programming language.",

    "ai": "AI stands for Artificial Intelligence. It helps machines think and learn like humans.",

    "html": "HTML is used to create the structure of websites.",

    "css": "CSS is used to style and design web pages.",

    "javascript": "JavaScript is used to add interactivity to websites.",

    "machine learning": "Machine Learning is a branch of AI where systems learn from data.",

    "nlp": "NLP means Natural Language Processing. It helps computers understand human language.",

    "streamlit": "Streamlit is a Python framework used to build web applications easily.",

    "react": "React is a JavaScript library used for frontend web development.",

    "sql": "SQL is used to store and manage data in databases.",

    "data science": "Data Science is the process of analyzing and understanding data."
}

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ----------------

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f'<div class="user-msg">👤 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot-msg">🤖 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# ---------------- CHAT INPUT ----------------

user_input = st.chat_input("Type your message here...")

# ---------------- BOT RESPONSE ----------------

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    question = user_input.lower()

    # Default response
    answer = """
🤖 I am still learning.

Please ask questions related to:
• Python
• AI
• HTML
• CSS
• JavaScript
• Machine Learning
• NLP
"""

    # FAQ Matching
    for key in faq:
        if key in question:
            answer = faq[key]
            break

    # Store bot response
    st.session_state.messages.append(
        {
            "role": "bot",
            "content": answer
        }
    )

    st.rerun()