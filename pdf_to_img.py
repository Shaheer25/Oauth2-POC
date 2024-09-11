import os
from PIL import Image as PILImage
import fitz

def convert_pdf_to_images(pdf_path, output_dir='C:/Users/Shaheer/OneDrive/Desktop/Office-365-POC-Flask/tmp/', dpi=300):
    doc = fitz.open(pdf_path)
    image_paths = []
    for i in range(len(doc)):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=dpi)
        pil_image = PILImage.frombytes("RGB", [pix.width, pix.height], pix.samples)
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"page_{i + 1}.png")
        pil_image.save(output_file, dpi=(dpi, dpi))  # Set DPI for saving image
        image_paths.append(output_file)
    doc.close()
    return image_paths

# Example usage:
pdf_file = 'brand.pdf'
output_directory = 'C:/Users/Shaheer/OneDrive/Desktop/Office-365-POC-Flask/tmp/'
image_paths = convert_pdf_to_images(pdf_file, output_dir=output_directory, dpi=300)

print("Images converted and saved to:")
for image_path in image_paths:
    print(image_path)
