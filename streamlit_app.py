from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Свечка за трафик",
    page_icon="🕯️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      header {visibility: hidden;}
      footer {visibility: hidden;}
      .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
      }
      iframe {
        display: block;
        margin: 0 auto;
        border-radius: 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

components.html(html, height=760, scrolling=False)
