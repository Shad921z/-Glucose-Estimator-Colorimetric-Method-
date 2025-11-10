import streamlit as st

# Add background image using CSS
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

st.markdown("# 👋 Hi, I'm Shad")
st.markdown("---")
st.markdown("""
I'm a Life Sciences student exploring Python, biotech tools, and Streamlit apps.
I build tools to analyze biochemical data and automate tasks in research.
""")
st.markdown("---")
st.markdown("### 📫 Connect with me")

st.markdown("""
<style>
.icon-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}
.icon-row img {
    filter: brightness(0) invert(1);
}
</style>

<div class='icon-row'>
    <img src='https://img.icons8.com/ios-glyphs/30/github.png'/>
    <a href='https://github.com/shad921z' target='_blank' style='color:white; text-decoration:none;'>@shad921z</a>
</div>

<div class='icon-row'>
    <img src='https://img.icons8.com/ios-filled/30/linkedin.png'/>
    <a href='https://linkedin.com/in/shadkhan921z' target='_blank' style='color:white; text-decoration:none;'>@shadkhan921z</a>
</div>

<div class='icon-row'>
    <img src='https://img.icons8.com/ios-filled/30/twitterx.png'/>
    <a href='https://twitter.com/shadkhan012' target='_blank' style='color:white; text-decoration:none;'>@shadkhan012</a>
</div>

<div class='icon-row'>
    <img src='https://img.icons8.com/ios-glyphs/30/new-post.png'/>
    <a href='mailto:shadkhan921z@gmail.com' style='color:white; text-decoration:none;'>shadkhan921z@gmail.com</a>
</div>
""", unsafe_allow_html=True)

