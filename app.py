import os
from pathlib import Path
import streamlit as st
from utils.transcriber import transcribe_video

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

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

    if video_file:

        file_path = UPLOAD_DIR / video_file.name

        with open(file_path, "wb") as f:
            f.write(video_file.getbuffer())
        with st.spinner("Generating transcript..."):
             transcript = transcribe_video(file_path)
        st.session_state.transcript = transcript     
        st.success("Transcript generated successfully!")    

        st.success("Video uploaded successfully!")

        st.write(f"Saved to: {file_path}")

    elif youtube_url:

        st.success("YouTube URL received!")

        st.write(youtube_url)

    else:

        st.warning("Please upload a video or provide a YouTube URL.")

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

    if "transcript" in st.session_state:
        st.write(st.session_state.transcript)

    else:
        st.info("Transcript will appear here")    

with translation_tab:
    st.info("Translation will appear here")

with notes_tab:
    st.info("Notes will appear here")

with quiz_tab:
    st.info("Quiz will appear here")