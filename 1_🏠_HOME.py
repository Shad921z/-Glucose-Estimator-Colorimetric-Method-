import streamlit as st

# Add background image using CSS
with st.container():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://wallpapers.com/images/high/dark-gradient-8km5m3gxmp08ny0f.webp");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

