import requests
from PIL import Image
from io import BytesIO

def decrease_dpi(image_url, output_file_path, target_dpi=75):
    # Download the image from the URL
    response = requests.get(image_url)
    if response.status_code != 200:
        raise Exception('Failed to download image')

    # Open the image
    img = Image.open(BytesIO(response.content))

    # Get the current DPI
    current_dpi = img.info.get('dpi', (300, 300))[0]  # Assume 300 DPI if not specified
    scale_factor = current_dpi / target_dpi

    # Calculate the new dimensions
    new_width = int(img.width / scale_factor)
    new_height = int(img.height / scale_factor)

    # Resize the image
    img_resized = img.resize((new_width, new_height))

    # Save the resized image with the new DPI
    img_resized.save(output_file_path, dpi=(target_dpi, target_dpi))

    print(f'Image saved to {output_file_path} with decreased DPI.')

# Example usage
image_url = 'https://einstonlabs.blr1.digitaloceanspaces.com/deck/cbd5d717-b0dc-4e0a-9a2d-3d6348575991/9766e082-c75f-400e-9f0d-f021265ef6cf.png'
output_file_path = 'output_image.png'

decrease_dpi(image_url, output_file_path)
