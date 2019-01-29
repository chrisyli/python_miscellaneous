import os
os.chdir("C:/Users/Yunsun CTR Li/Desktop/PyPdf")

from PyPDF2 import PdfFileMerger

pdfs = ["phone Jan.pdf", "Your AT&T bill.pdf"]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, "rb"))

with open("result.pdf", "wb") as output:
    merger.write(output)