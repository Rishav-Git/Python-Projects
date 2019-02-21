## Merge all pdf files in a folder
import os
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
 
def merger(output_path, input_paths,now):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh) 
 
if __name__ == '__main__':
    path = input("Enter the path: ")
    now = os.getcwd()
    os.chdir(path)
    paths = glob.glob('*.pdf')
    paths.sort()
    merger('pdf_merged.pdf', paths,now)
