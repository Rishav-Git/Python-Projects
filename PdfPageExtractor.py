import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import shutil
import re
from pathlib import Path

def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)
    

def pdf_splitter(path,no1,no2):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(no1,no2):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)


if __name__ == '__main__':
    path = input("Enter the path:")
    no1 = input("Enter the starting page number:")
    no1=int(no1)-1
    no2 = input("Enter the last page:")
    no2=int(no2)
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf_splitter(path,no1,no2)
    paths = glob.glob('{}_page_*.pdf'.format(fname))
    paths.sort()
    new = input("Enter the name of the pdf file to be created:")
    merger(new, paths)
    for p in Path(".").glob('{}_page_*.pdf'.format(fname)):
        p.unlink()
    
    

 
