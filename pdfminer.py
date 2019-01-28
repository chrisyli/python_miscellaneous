import os
os.chdir("...")
print(os.listdir(os.getcwd()))

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
#from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams(char_margin=10, line_margin=0.5, word_margin=0.1)
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    file = open(path, "rb")
    interpreter = PDFPageInterpreter(rsrcmgr, device) 
#    ltpages = []
    for page in PDFPage.get_pages(file):
        interpreter.process_page(page)
#        ltpages.append(device.get_result())
    text = retstr.getvalue()
    file.close()
    device.close()
    retstr.close()
    return text
#    return ltpages

all_text = convert_pdf_to_txt("2019-01-20.pdf")
type(all_text)

# Remove line breaks, etc.
import re
all_text = re.sub(r"\n", " ", all_text)
all_text = re.sub(r"\x0c", " ", all_text)
all_text = re.sub(r"\t", " ", all_text)
all_text = re.sub(r"\v", " ", all_text)
print(len(all_text))