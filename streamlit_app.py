import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Свечка за трафик",
    page_icon="🕯️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #0b0b10 !important;
      }
      .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 1120px !important;
      }
      header, footer, #MainMenu, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
      }
      iframe {
        display: block !important;
        margin: 0 auto !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")
components.html(html, height=960, scrolling=True)
