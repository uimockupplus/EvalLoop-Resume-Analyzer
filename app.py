from pydf import PdfReader
pdf_path = "resumes/Kaneti_Vivek_Resume.pdf"
reader = PdfReader(pdf_path)
text=" "
for page in reader.pages:
  text += pages.extract_text() or " "
  print("______Resume Text_______")
  print (text)
