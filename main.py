import streamlit as st

def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('main.py', label='Welcome', icon='🔥')
        st.page_link('pages/1_movement_tool.py', label='Movement Tool', icon='🛡️')
        st.page_link('pages/2_advance_help.py', label='Advance Help', icon='🛡️')
        st.page_link('pages/3_city_calculator.py', label='City Calculator', icon='🛡️')
        st.page_link('pages/4_calamities.py', label='Calamities', icon='🛡️')
    st.title(f'🔥 Individual Checker')

'''st.set_page_config(
    page_title="Game Assistance App",
    page_icon="🎲",
    layout="wide",
)'''

'''# Main page content
st.title("Game Assistance App")
st.write("""
Welcome to the multi-functional game assistance app! Use the sidebar to navigate between different tools: 
- Movement Tool
- Advancement Helper
- City Calculator
- Calamities Overview
""")'''

if __name__ == '__main__':
    main()