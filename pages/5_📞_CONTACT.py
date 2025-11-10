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

    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/shadkhan921z@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")