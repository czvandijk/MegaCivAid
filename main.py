import streamlit as st

st.sidebar.header("Welcome")

st.set_page_config(
    page_title="Game Assistance App",
    page_icon="🎲",
    layout="wide",
)

# Main page content
st.title("Game Assistance App")
st.write("""
Welcome to the multi-functional game assistance app! Use the sidebar to navigate between different tools: 
- Movement Tool
- Advancement Helper
- City Calculator
- Calamities Overview
""")
