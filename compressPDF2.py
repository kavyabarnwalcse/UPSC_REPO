import pdfrw

# Open the PDF file
input_pdf = pdfrw.PdfReader('January.pdf')

# Set the compression level (0-9, 9 being strongest compression)
output_pdf = pdfrw.PdfWriter('January_merged2.pdf', compress_level=9)

# Add each page of the PDF to the output PDF writer
for page in input_pdf.pages:
    output_pdf.addpage(page)

# Save the compressed PDF file
output_pdf.write()
