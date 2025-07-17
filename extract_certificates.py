#!/usr/bin/env python3
import os
from pdf2image import convert_from_path
import sys

def extract_certificates():
    """Extract individual certificates from combined_certificates.pdf"""
    
    # Paths
    pdf_path = 'Photos/combined_certificates.pdf'
    output_dir = 'Photos/certificates'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Convert PDF to images
        print("Converting PDF to images...")
        images = convert_from_path(pdf_path, dpi=300, fmt='jpeg')
        
        print(f"Found {len(images)} certificates")
        
        # Save each certificate as a separate image
        for i, image in enumerate(images, 1):
            output_path = os.path.join(output_dir, f'certificate_{i:02d}.jpg')
            image.save(output_path, 'JPEG', quality=95)
            print(f"Saved: certificate_{i:02d}.jpg")
        
        print(f"\nSuccessfully extracted {len(images)} certificates to {output_dir}/")
        return len(images)
        
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    extract_certificates()
