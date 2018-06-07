import docx
from docx import Document
from docx.shared import Inches
doc = docx.Document('demo.docx')
fulltext=[];
for para in doc.paragraphs:
    fulltext.append(para.text)

print('\n'.join(fulltext))
