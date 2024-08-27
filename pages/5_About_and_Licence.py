import streamlit as st

def license_and_info():
    # Page title
    st.title("License and Information")
    
    # App information section
    st.header("App Information")
    st.write("This web app was built to provide tools for the board game Mega Civilization. "
             "It includes features such as a movement tool, advancement help, a city calculator, and a calamities overview.")
    
    # License section
    st.header("License")
    st.write("This app is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International License.")
    st.write("[Learn more about this license](https://creativecommons.org/licenses/by-nc-sa/4.0/).")
    
    # Attribution section
    st.header("Attribution")
    st.write("This app is based on work originally created by **Matt Crawford**.")
    st.write("You are free to share and adapt the material in this app under the terms of the "
             "Attribution-NonCommercial-ShareAlike 4.0 International License.")
    
    # Developer information
    st.header("Developer Information")
    st.write("Created by **Chris van Dijk**.")
    st.write("If you have any questions or suggestions, feel free to contact me at: "
             "[mega-civ-aid@chrisvandijk.nl](mailto:mega-civ-aid@chrisvandijk.nl)")
    
    # Buy Me a Coffee
    st.write("If you'd like to support my work, feel free to [buy me a coffee](https://buymeacoffee.com/chrisvandijk)!")
