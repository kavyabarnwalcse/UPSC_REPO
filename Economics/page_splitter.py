#Import pypdf2
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import sys

def page_split(path,startPage,steps):
  with open(path, 'rb') as f:
      pdf = PdfFileReader(f)
      number_of_pages = pdf.getNumPages()
      pdfWriter = PdfFileWriter()
      for i in range(startPage,number_of_pages,steps):
        page = pdf.getPage(i)
        pdfWriter.addPage(page)
      resultPdfFile = open(path[:path.find('.pdf')]+'_splitted_'+str(startPage)+'_'+str(number_of_pages)+'_'+str(steps)+'.pdf', 'wb')
      pdfWriter.write(resultPdfFile)
      resultPdfFile.close()

if(__name__=='__main__'):
    if(len(sys.argv)==4):
        path=sys.argv[1]
        startPage=int(sys.argv[2])
        steps=int(sys.argv[3])
        page_split(path,startPage,steps)
    else:
        print(len(sys.argv),' Pass filepath, start and steps')