from pathlib import Path
import streamlit as st

from utils.transcriber import transcribe_video
from utils.notes_generator import generate_notes
from utils.quiz_generator import generate_quiz

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
            # ------------------------------------------
            # Generate Quiz
            # ------------------------------------------
            with st.spinner("Generating quiz..."):
                 quiz = generate_quiz(
                      transcript[:5000]
                      )
            st.session_state.quiz = quiz
            st.success("Quiz generated successfully!")

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

    if "quiz" in st.session_state:

        quiz = st.session_state.quiz

        st.subheader("Interactive Quiz")

        with st.form("quiz_form"):

            user_answers = []

            for i, q in enumerate(quiz):

                answer = st.radio(
                    f"Q{i+1}. {q['question']}",
                    q["options"],
                    key=f"q_{i}"
                )

                user_answers.append(answer)

            submitted = st.form_submit_button(
                "Submit Quiz"
            )

        if submitted:

            score = 0

            st.markdown("---")
            st.subheader("Results")

            for i, q in enumerate(quiz):

                user_answer = user_answers[i]
                correct_answer = q["answer"]

                if user_answer == correct_answer:

                    score += 1

                    st.success(
                        f"Q{i+1}: Correct"
                    )

                else:

                    st.error(
                        f"Q{i+1}: Incorrect"
                    )

                    st.write(
                        f"Your Answer: {user_answer}"
                    )

                    st.write(
                        f"Correct Answer: {correct_answer}"
                    )

                    if "explanation" in q:

                        st.info(
                            f"Explanation: {q['explanation']}"
                        )

                st.markdown("---")

            st.success(
                f"🎯 Final Score: {score}/{len(quiz)}"
            )

    else:

        st.info(
            "Quiz will appear here"
        )