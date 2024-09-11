import subprocess
import os

def convert_pptx_to_pdf(pptx_path, output_pdf_path):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_pdf_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Run LibreOffice in headless mode to convert PPTX to PDF
    subprocess.run([
        'libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', output_dir, pptx_path
    ], check=True)

    print(f"Converted {pptx_path} to PDF at {output_pdf_path}")

# Example usage
convert_pptx_to_pdf('spp.ppt', 'output_pdf/jwt.pdf')
