from pypdf import PdfReader

reader = PdfReader('stanford_lecture_guide.pdf')
pdf = ''

for i in range(len(reader.pages)):
    pdf = reader.pages[i].extract_text()

print(pdf)