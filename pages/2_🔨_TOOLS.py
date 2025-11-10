import streamlit as st

st.set_page_config(layout="wide")

# Background
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

st.markdown("# 🧰 My Tools")

tools = [
    {
        "name": "Glucose Analyzer",
        "image": "https://img.icons8.com/fluency/48/test-tube.png",
        "desc": "Check blood glucose levels and get health insights.",
        "page": "/glucoseEstimator"
    },
    {
        "name": "Protein Estimator",
        "image": "https://img.icons8.com/fluency/48/protein.png",
        "desc": "COMING SOON.",
        "page": None
    },
    {
        "name": "Cholesterol Tracker",
        "image": "https://img.icons8.com/fluency/48/heart-with-pulse.png",
        "desc": "COMING SOON.",
        "page": None
    },
]

# Card styling
st.markdown("""
<style>
.tool-card {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    display: flex;
    gap: 20px;
    align-items: center;
    margin-bottom: 15px;
    color: white;
}
.tool-card img {
    width: 48px;
    height: 48px;
}
.tool-card h4 {
    margin: 0;
}
.tool-card p {
    margin: 5px 0 0;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Cards with buttons
for tool in tools:
    st.markdown(f"""
    <div class='tool-card'>
        <img src='{tool["image"]}' />
        <div>
            <h4>{tool["name"]}</h4>
            <p>{tool["desc"]}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if tool.get("page"):
        st.link_button(f"Open {tool['name']}", tool["page"])
