from pypdf import PdfReader

pdf_path = "resumes/my_resume.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text() or ""
    text += page_text

print("----- RESUME TEXT -----")
print(text)
print("-----------------------")
