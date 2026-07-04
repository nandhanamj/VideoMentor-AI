import ollama


def generate_notes(transcript):

    prompt = f"""
    Create structured study notes from the following transcript.

    Include:
    1. Summary
    2. Key Concepts
    3. Important Points

    Transcript:
    {transcript}
    """

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]