import ollama
import json


def generate_quiz(transcript):

    prompt = f"""
Create exactly 5 multiple-choice questions.

Return ONLY valid JSON.

Each question must contain:

- question
- options
- answer
- explanation

Format:

[
  {{
    "question": "...",
    "options": [
      "...",
      "...",
      "...",
      "..."
    ],
    "answer": "...",
    "explanation": "..."
  }}
]

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

    content = response["message"]["content"]

    # Remove markdown fences if Gemma adds them
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    return json.loads(content)