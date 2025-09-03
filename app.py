import streamlit as st
from transformers import pipeline
from PIL import Image

# -----------------------------
# Streamlit Page Config & Styling
# -----------------------------
st.set_page_config(page_title="Text Summarizer App", page_icon="📝", layout="wide")

# Optional background image
def set_bg(png_file):
    from pathlib import Path
    import base64
    if Path(png_file).exists():
        with open(png_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Call the function if you have a background image
# set_bg("background.png")

# Custom CSS for styling
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}
h1 {
    color: #4b0082;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# App Title
# -----------------------------
st.title("📝 Text Summarizer App")
st.markdown("Enter a paragraph, and get a concise summary instantly!")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Settings")
max_len = st.sidebar.slider("Max Summary Length", min_value=30, max_value=300, value=120)
min_len = st.sidebar.slider("Min Summary Length", min_value=10, max_value=100, value=30)

# -----------------------------
# Main Layout
# -----------------------------
col1, col2 = st.columns([1,1])

with col1:
    st.header("Enter Text")
    user_input = st.text_area("Type or paste your paragraph here:", height=250)

with col2:
    st.header("Summary Output")
    if st.button("Summarize"):
        if user_input.strip():
            with st.spinner("Summarizing..."):
                summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                summary = summarizer(user_input, max_length=max_len, min_length=min_len, do_sample=False)
                st.success("✅ Summary generated!")
                st.markdown("### Summary:")
                st.write(summary[0]['summary_text'])
        else:
            st.warning("⚠️ Please enter some text to summarize!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("© 2025 Text Summarizer App | Built with Python & Streamlit 💻")
