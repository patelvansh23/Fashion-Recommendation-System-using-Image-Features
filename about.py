import streamlit as st

def run_about():
    st.title("About Us")
    st.write("""The Fashion is more than just clothing; it's a profound form of self-expression.
It reflects our personalities, moods, and even our aspirations. Throughout history, fashion has evolved, influenced by cultural shifts, technological advancements, and individual creativity. 
From classic styles that stand the test of time to modern trends that push boundaries, fashion serves as a canvas for individuals to showcase their uniqueness.      
Whether it's a casual outfit or a formal ensemble, each piece tells a story and can evoke a sense of confidence and identity.""")
    
    image_path = "backgroud2.jpg"  # Make sure the path is correct
    st.image(image_path, use_column_width=True)

