
from text_processor import chunk_text
from summarizer import generate_notes

lecture_text = """
Artificial Intelligence is a branch of computer science
that focuses on developing machines capable of performing
tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.
It enables computers to learn from data without being
explicitly programmed.

Deep Learning is a subset of Machine Learning.
It uses artificial neural networks to identify complex
patterns in large amounts of data.

Neural networks consist of interconnected nodes that
process information and help computers learn patterns.
"""

chunks = chunk_text(lecture_text, chunk_size=50, overlap=10)

notes = generate_notes(chunks)

print("\n========== FINAL LECTURE NOTES ==========\n")
print(notes)
