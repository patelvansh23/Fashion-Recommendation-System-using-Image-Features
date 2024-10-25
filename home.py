import streamlit as st
from PIL import Image
from io import BytesIO
import base64

def show_app():
    st.session_state.page = "app"

def show_about():
    st.session_state.page = "about"

def show_home():
    image_path = "backgroud.jpg"  # Make sure the path is correct
    bg_image = Image.open(image_path)

    def image_to_base64(image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{image_to_base64(bg_image)}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .title-text {{
            color: White;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            font-size: 4em;
            font-weight: bold;
        }}
        .welcome-text {{
            color: #cc8262;
            font-size: 1.5em;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title-text">Fashion Fusion</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-text">Welcome to Fashion Fusion</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
