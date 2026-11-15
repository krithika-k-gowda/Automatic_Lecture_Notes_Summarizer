from text_processor import chunk_text
sample_text="""Artificial Intelligence is a branch of computer science.Machine Learning is a subset of artificial intelligence.Deep Learning uses neural networks to learn complex patterns."""
chunks=chunk_text(sample_text,chunk_size=10,overlap=2)
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)