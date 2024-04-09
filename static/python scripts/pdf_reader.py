# This module is used to extract text from the pdf document
from PyPDF2 import PdfReader

def pdf_data(PDF_FILE):
    '''This function takes file location(PDF) as a string in the input and returns a list containing all the words in the pdf'''

    pdfreader = PdfReader(PDF_FILE)
    
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content

    # spliting the raw_text by '\n'
    data = raw_text.split('\n')
    
    return data

def pdf_pages(PDF_FILE):
    '''This function takes file location(PDF) as a string in the input and returns the number of pages in the pdf'''

    pdfreader = PdfReader(PDF_FILE)
    
    return len(pdfreader.pages) 


# PDF_FILE = "E:\Projects\Spell Checker\Spell_Checker\static\dataset\words.pdf"
# data = pdf_data(PDF_FILE)
# print(data)
