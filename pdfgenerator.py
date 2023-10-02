from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF file
pdf_file = "decklist.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Add text to the PDF
c.drawString(35, 750, "Last Name : ")
c.drawString(35, 730, "First Name : ")
c.drawString(35, 710, "One piece ID : ")
c.drawString(350, 750,"Event : ")
c.drawString(350, 730,"Date : ")

# Draw a rectangle
c.rect(25, 650, 562, 2, fill=1)

# Save the PDF file
c.save()

print(f"The decklist '{pdf_file}' was created successfully.")