import pymupdf4llm


def parse_pdf(pdf_path: str) -> list[str]:
    markdown = pymupdf4llm.to_markdown(pdf_path)

    sections = markdown.split("\n# ")

    cleaned_sections = []

    for section in sections:
        section = section.strip()

        if len(section) > 100:
            cleaned_sections.append(section)

    return cleaned_sections
