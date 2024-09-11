import fitz  # PyMuPDF library
import os

def remove_watermark_from_pdf(pdf_path, output_dir=None):
    try:
        if output_dir is None:
            output_dir = os.path.dirname(pdf_path)
        
        pdf_document = fitz.open(pdf_path)
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            
            # Search for the exact text watermark
            text_instances = page.search_for("Evaluation Warning : The document was created with Spire.Presentation for Python")
            
            for inst in text_instances:
                # Clear the area occupied by the watermark
                rect = fitz.Rect(inst)  # Convert instance to rectangle
                page.drawRect(rect)  # Clear the rectangle area
            
        # Save the modified PDF
        output_pdf_path = os.path.join(output_dir, "Modified_" + os.path.basename(pdf_path))
        pdf_document.save(output_pdf_path)
        pdf_document.close()
        print(f"Watermarks removed from {pdf_path} and saved as {output_pdf_path}")
        return output_pdf_path
    
    except Exception as e:
        print(f"Error removing watermarks from {pdf_path}: {str(e)}")
        return None

# Example usage:
# remove_watermark_from_pdf('PresentationToPDF.pdf')

    
# remove_watermark_from_pdf('PresentationToPDF.pdf',"C:/Users/Shaheer/OneDrive/Desktop/Office-365-POC-Flask")

from PyPDF2 import PdfReader, PdfWriter 
from PyPDF2.generic import TextStringObject, NameObject , ContentStream 
def b_(s):
    if type(s) == bytes:
        return s
    else:
        try:
            r = s.encode("latin-1")
            return r
        except Exception:
            r = s.encode("utf-8")
            return r

def remove_watermark_from_pdf(input_pdf_path, output_pdf_path, watermark_text):
    try:
        # Open the input PDF file
        with open(input_pdf_path, "rb") as input_stream:
            source = PdfReader(input_stream)
            output = PdfWriter()

            # For each page in the PDF
            for page_num in range(source.numPages):
                page = source.getPage(page_num)
                content_object = page["/Contents"].getObject()
                content = ContentStream(content_object, source)

                # Loop over all PDF elements
                for operands, operator in content.operations:
                    if operator == b_("TJ"):
                        # Check if the operand is a TextStringObject and starts with the watermark text
                        text = operands[0][0]
                        if isinstance(text, TextStringObject) and text.startswith(watermark_text):
                            operands[0] = TextStringObject(" ")  # Replace watermark with an empty string

                # Set the modified content as content object on the page
                page.__setitem__(NameObject('/Contents'), content)

                # Add the modified page to the output PDF
                output.addPage(page)

            # Write the modified PDF to output file
            with open(output_pdf_path, "wb") as output_stream:
                output.write(output_stream)

            print(f"Watermarks removed from {input_pdf_path} and saved as {output_pdf_path}")
            return output_pdf_path

    except Exception as e:
        print(f"Error removing watermarks from {input_pdf_path}: {str(e)}")
        return None

# Example usage:
input_pdf_file = 'PresentationToPDF.pdf'
output_pdf_file = 'Modified_PresentationToPDF.pdf'
watermark_text = 'Evaluation Warning : The document was created with Spire.Presentation for Python'

remove_watermark_from_pdf(input_pdf_file, output_pdf_file, watermark_text)