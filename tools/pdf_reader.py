try:
    import PyPDF2
except ImportError:
    PyPDF2 = None


def read_pdf(path: str) -> str:
    if PyPDF2 is None:
        return "PyPDF2 not installed"

    text = []
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text.append(page.extract_text() or "")
    return "\n".join(text)
