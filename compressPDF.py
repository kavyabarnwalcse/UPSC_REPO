import PyPDF2

# Open the input PDF file
input_file = open('January.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(input_file)

# Create a new PDF file writer
pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the pages of the input PDF file
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)
    
    # Compress the page content
    page.compressContentStreams()
    
    # Add the compressed page to the output PDF file
    pdf_writer.addPage(page)

# Write the compressed PDF file to disk
output_file = open('January_compressed.pdf', 'wb')
pdf_writer.write(output_file)

# Close the input and output files
input_file.close()
output_file.close()
