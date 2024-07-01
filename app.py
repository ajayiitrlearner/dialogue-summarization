import streamlit as st

# Set page configuration
st.set_page_config(page_title="Dialogue Summarization Tool", page_icon=":robot_face:", layout="wide")

# Page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Summarization"])

if page == "Overview":
    import overview
    overview.show()
else:
    import summarization
    summarization.show()
