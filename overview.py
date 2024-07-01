import streamlit as st

def show():
    st.title("Dialogue Summarization Tool")
    st.write("""
    The automated dialogue transcript summarization tool is designed to effortlessly condense dialogue transcripts,
    providing users with powerful features for summarizing text documents. Whether manually inputting text or uploading
    PDF documents, this tool caters to various needs, significantly boosting productivity.
    """)

    st.header("Top Features")

    st.write("""
    - **Flexible Input Options**: Users can either manually enter text or upload PDF documents for summarization, offering versatility and convenience.
    - **Lighter Machine Learning Models**: Leveraging the latest in machine learning technology, the tool utilizes simpler LLMs with < 1B parameters to produce precise and concise summaries tailored to the specific input.
    - **Customized Summaries**: The generated summaries are specifically tailored to the provided content, ensuring they are both relevant and accurate.
    - **Boosted Productivity**: By automating the summarization process, the tool significantly reduces the time and effort needed for information extraction, thereby enhancing productivity.
    - **User-Friendly Interface**: Featuring an intuitive interface, the application ensures a smooth and efficient user experience, making it easy for users to access and utilize its powerful summarization capabilities.
    """)
