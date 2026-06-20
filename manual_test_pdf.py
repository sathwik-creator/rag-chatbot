from src.pdf_loader import load_pdf

documents = load_pdf("uploads/sample.pdf")

print("Pages:", len(documents))

for i, doc in enumerate(documents):
    print(f"\n--- PAGE {i + 1} ---")
    print("Length:", len(doc.page_content))
    print(repr(doc.page_content[:100]))
