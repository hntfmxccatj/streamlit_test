import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(
    page_title="食谱推荐",
    page_icon="🍳",
)


#隐藏streamlit自带的功能按钮
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown('# 🏠 食谱推荐')


def main():
    st.markdown("# *What's Cooking? :cooking:*")

if __name__ == "__main__":
    main()


st.markdown(
        "#### Given a list of ingredients, what different recipes can I can make? :tomato: "
    )
