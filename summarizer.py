
import requests


def summarize_chunk(text):

    prompt = f"""
    You are a lecture notes assistant.

    Summarize the following lecture content.
    Follow these instructions:
    - Use short bullet points.
    - Include important concepts and definitions.
    - Avoid unnecessary explanations.
    - Do not add information that is not in the lecture.

    Lecture content:
    {text}

    Summary:
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False
            },
            timeout=500
        )

        response.raise_for_status()

        result = response.json()

        return result["response"].strip()

    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"


def generate_notes(chunks):

    summaries = []

    for i, chunk in enumerate(chunks):

        print(f"Summarizing chunk {i + 1}...")

        summary = summarize_chunk(chunk)

        summaries.append(summary)

    final_notes = "\n".join(summaries)

    return final_notes
