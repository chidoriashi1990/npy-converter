import streamlit as st

from pages import dashboard


def main():
    st.title("converts npy files to csv files")
    dashboard.display()


if __name__ == "__main__":
    main()
