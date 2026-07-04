import streamlit as st

st.set_page_config(
    page_title="VideoMentor AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 VideoMentor AI")
st.subheader("Transform Videos into Learning Materials")

st.markdown("---")

# Input Method
input_type = st.radio(
    "Choose Input Type",
    ["Upload Video", "YouTube URL"]
)

video_file = None
youtube_url = ""

if input_type == "Upload Video":
    video_file = st.file_uploader(
        "Upload a Video",
        type=["mp4", "avi", "mov", "mkv"]
    )

else:
    youtube_url = st.text_input(
        "Enter YouTube URL"
    )

language = st.selectbox(
    "Select Output Language",
    [
        "English",
        "Malayalam",
        "Hindi",
        "Tamil",
        "Arabic"
    ]
)

if st.button("Process Video"):
    st.success("Phase 1 UI Working Successfully!")

    if video_file:
        st.write("Uploaded:", video_file.name)

    if youtube_url:
        st.write("URL:", youtube_url)

    st.write("Selected Language:", language)

st.markdown("---")

st.header("Output")

transcript_tab, translation_tab, notes_tab, quiz_tab = st.tabs(
    [
        "Transcript",
        "Translation",
        "Notes",
        "Quiz"
    ]
)

with transcript_tab:
    st.info("Transcript will appear here")

with translation_tab:
    st.info("Translation will appear here")

with notes_tab:
    st.info("Notes will appear here")

with quiz_tab:
    st.info("Quiz will appear here")