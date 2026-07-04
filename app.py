from pathlib import Path
import streamlit as st

from utils.transcriber import transcribe_video
from utils.notes_generator import generate_notes

# ==================================================
# Create required directories
# ==================================================

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# ==================================================
# Streamlit Configuration
# ==================================================

st.set_page_config(
    page_title="VideoMentor AI",
    page_icon="🎓",
    layout="wide"
)

# ==================================================
# Header
# ==================================================

st.title("🎓 VideoMentor AI")
st.subheader("Transform Videos into Learning Materials")

st.markdown("---")

# ==================================================
# Input Type Selection
# ==================================================

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

# ==================================================
# Language Selection (for future translation feature)
# ==================================================

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

# ==================================================
# Process Button
# ==================================================

if st.button("Process Video"):

    if video_file:

        try:

            # ------------------------------------------
            # Save Uploaded Video
            # ------------------------------------------

            file_path = UPLOAD_DIR / video_file.name

            with open(file_path, "wb") as f:
                f.write(video_file.getbuffer())

            st.success("Video uploaded successfully!")

            st.write(f"Saved to: {file_path}")

            # ------------------------------------------
            # Generate Transcript
            # ------------------------------------------

            with st.spinner("Generating transcript..."):

                transcript = transcribe_video(file_path)

            st.session_state.transcript = transcript

            st.success("Transcript generated successfully!")

            # ------------------------------------------
            # Generate Notes
            # ------------------------------------------

            with st.spinner("Generating study notes..."):

                notes = generate_notes(
                    transcript[:5000]
                )

            st.session_state.notes = notes

            st.success("Study notes generated successfully!")

        except Exception as e:

            st.error(
                f"Processing failed: {str(e)}"
            )

    elif youtube_url:

        st.success("YouTube URL received!")

        st.write(youtube_url)

        st.info(
            "YouTube processing will be implemented in a later phase."
        )

    else:

        st.warning(
            "Please upload a video or provide a YouTube URL."
        )

# ==================================================
# Output Section
# ==================================================

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

# ==================================================
# Transcript Tab
# ==================================================

with transcript_tab:

    if "transcript" in st.session_state:

        st.write(
            st.session_state.transcript
        )

    else:

        st.info(
            "Transcript will appear here"
        )

# ==================================================
# Translation Tab
# ==================================================

with translation_tab:

    st.info(
        "Translation feature coming soon."
    )

# ==================================================
# Notes Tab
# ==================================================

with notes_tab:

    if "notes" in st.session_state:

        st.write(
            st.session_state.notes
        )

    else:

        st.info(
            "Study notes will appear here"
        )

# ==================================================
# Quiz Tab
# ==================================================

with quiz_tab:

    st.info(
        "Quiz feature coming soon."
    )