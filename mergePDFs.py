import os
import PyPDF2
import sys

print("Please run the script as:\n'python mergePDFs.py .\path\\to\\folder(say .\DCA\Febrarury) pageNumberToStartFrom(say 2)'")

if len(sys.argv) < 3:
    print("Please provide Folder Path.")
    sys.exit()

input_folder =  sys.argv[1] #'./DCA/Febraury'  # input folder containing PDF files
output_pdf = 'merged.pdf'  # output PDF file name
start_page = int(sys.argv[2])  # starting page number
end_page = 5  # ending page number

# get a list of PDF files in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

# sort the files based on the modification time
sorted_files = sorted(pdf_files, key=lambda x: os.path.getmtime(os.path.join(input_folder, x)))

# open the output PDF file in write mode
output = PyPDF2.PdfFileWriter()

# merge the PDF files and pages
for file in sorted_files:
    print("Merging File: {0}".format(file), end=", ")
    # open the PDF file in read mode
    input_file = PyPDF2.PdfFileReader(open(os.path.join(input_folder, file), 'rb'))

    # get the number of pages in the PDF file
    num_pages = input_file.getNumPages()
    end_page = num_pages
    print('From Page #{0} to #{1}'.format(start_page, end_page))
    # add the pages of the PDF file to the output PDF file
    for page_num in range(start_page-1, end_page):
        page = input_file.getPage(page_num)
        page.mergePage(page)
        output.addPage(page)

# add page numbers to the merged PDF file
for page_num in range(output.getNumPages()):
    page = output.getPage(page_num)

# write the output PDF file
with open(output_pdf, 'wb') as output_file:
    output.write(output_file)