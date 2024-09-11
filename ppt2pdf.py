from spire.presentation import Presentation , FileFormat
from pdf_to_img import convert_pdf_to_images

def convert_ppt_to_pdf(input_ppt_path, output_pdf_path):
    try:
        presentation = Presentation()
        presentation.LoadFromFile(input_ppt_path)
        presentation.SaveToFile(output_pdf_path, FileFormat.PDF)
        presentation.Dispose()
        print(f"Converted {input_ppt_path} to {output_pdf_path}")
    except Exception as e:
        print(f"Error converting {input_ppt_path} to PDF: {str(e)}")

input_ppt_file = "sa.pptx"
output_pdf_file = "PresentationToPDF.pdf"
convert_ppt_to_pdf(input_ppt_file, output_pdf_file)
convert_pdf_to_images(output_pdf_file)
