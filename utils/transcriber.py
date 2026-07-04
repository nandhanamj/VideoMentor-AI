import whisper
from pathlib import Path

# Load model once
model = whisper.load_model("base")

def transcribe_video(video_path):

    result = model.transcribe(str(video_path))

    transcript = result["text"]

    transcript_dir = Path("data/transcripts")
    transcript_dir.mkdir(parents=True, exist_ok=True)

    transcript_file = transcript_dir / f"{Path(video_path).stem}.txt"

    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript