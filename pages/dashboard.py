import streamlit as st

from services import file_service


def display():
    st.header("Upload .npy file")

    uploaded_file = st.file_uploader("Choose a CSV file", type="npy")
    if uploaded_file:
        data = file_service.read_npy(uploaded_file)
        st.dataframe(data)

        file_service.save_csv(data.to_numpy())

        st.success("success!", icon="✅")
        # st.link_button("📁 Go to folder", "temp/")
