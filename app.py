import streamlit as st
import pickle
import pandas as pd

def add_sidebar():
    st.sidebar.title("Cell Nuclei Measurements")


def main():
    st.set_page_config(
        page_title="Breast Cancer Prediction App",
        page_icon="🩺",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    add_sidebar()


    with st.container():
        st.title("Breast Cancer Prediction App")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar. ")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write('')

    with col2:
        st.image('assets/breast_cancer.png', width=200)

if __name__ == '__main__':
    main()