from pypdf import PdfReader
def extract_text_from_pdf(pdf_file):
    reader=PdfReader(pdf_file)
    extracted_text=""
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            extracted_text+=page_text+"\n"
    return extracted_text
def chunk_text(text,chunk_size=1000,overlap=50):
    words=text.split()
    chunks=[]
    start=0
    while start<len(words):
        end=start+chunk_size
        chunk=words[start:end]
        chunks.append(" ".join(chunk))
        start+=chunk_size-overlap
    return chunks