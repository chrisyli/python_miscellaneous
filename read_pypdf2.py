import os
print(os.getcwd())

from PyPDF2 import PdfFileReader

# Note there is no space between words extracted
fileObj = open("2019-01-20.pdf", "rb")
pdfreader = PdfFileReader(fileObj)

# Check individual page(s)
page1 = pdfreader.getPage(1)
print(page1.extractText())

# Define a function to read all pages (or page range)
def get_text(path):
    # Load PDF into PyPDF2
    pdfreader = PdfFileReader(open(path, "rb"))
    # Iterate over all pages
    content = ""
    for i in range(0, pdfreader.getNumPages()):
        content += pdfreader.getPage(i).extractText() + "\n"
    return content

get_text("document.pdf")
