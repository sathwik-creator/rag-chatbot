from src.chunking import chunk_documents
from src.pdf_loader import load_pdf

# Load PDF
documents = load_pdf("uploads/Dubakunta_Sathwik_Resume.pdf")

# Create chunks
chunks = chunk_documents(documents)

print("=" * 50)
print("CHUNKING TEST")
print("=" * 50)

print(f"Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")

print("\nFIRST CHUNK:")
print("-" * 50)
print(chunks[0].page_content)

print("\n")

if len(chunks) > 1:
    print("SECOND CHUNK:")
    print("-" * 50)
    print(chunks[1].page_content)

print("\n")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1} Length: {len(chunk.page_content)} characters")
