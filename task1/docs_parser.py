import io
import os
import subprocess

import docx2txt

from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams, LTTextBox


def save_doc_as_docx(file):
    
    pathf = os.getcwd()+"/files/"+file
    subprocess.call(['soffice', '--headless', '--convert-to', 'docx', '--outdir', 'files', pathf])
    

def write_to_file(name, value):
    file = "result/"+name+".txt"
    f = open(file, "w")
    f.write(value)
    f.close()


def docx_get_lines(file):
    pathf = os.getcwd()+"/files/"+file
    write_to_file(file, docx2txt.process(pathf))


def docx_get_lines_ret(file):
    pathf = os.getcwd()+"/files/"+file
    return docx2txt.process(pathf)

    
def pdf_get_lines(file):

    pathf = os.getcwd()+"/files/"+file

    fp = open(pathf, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    text = ''
    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, this_text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                if this_text != ("\n" or "" or " "):
                    text = text + this_text
   
    write_to_file(file, text)


def pdf_get_lines_ret(file):

    pathf = os.getcwd()+"/files/"+file

    fp = open(pathf, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    text = ''
    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, this_text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                if this_text != ("\n" or "" or " "):
                    text = text + this_text
    return(text)

