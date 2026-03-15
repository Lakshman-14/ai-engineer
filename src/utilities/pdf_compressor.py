import os
import sys
import pikepdf
import io
from PIL import Image

def compress_image(image_obj, quality=50):
    """
    Compresses a single image object using Pillow.
    Returns the compressed image bytes.
    """
    try:
        # pikepdf image extraction
        pdfimage = pikepdf.PdfImage(image_obj)
        pil_image = pdfimage.as_pil_image()
        
        # Convert to RGB if necessary (e.g. CMYK, RGBA, P) to save as JPEG
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
            
        output_buffer = io.BytesIO()
        pil_image.save(output_buffer, format='JPEG', quality=quality, optimize=True)
        return output_buffer.getvalue()
    except Exception as e:
        # print(f"Skipping image due to error: {e}")
        return None

def compress_pdf(input_file, output_file, target_size_mb=14):
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        return

    original_size = os.path.getsize(input_file)
    original_size_mb = original_size / (1024 * 1024)
    print(f"Original Size: {original_size_mb:.2f} MB")

    if original_size_mb <= target_size_mb:
        print(f"File is already smaller than {target_size_mb}MB.")
        # Just copy/save efficiently
        try:
            pdf = pikepdf.open(input_file)
            pdf.save(output_file, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
        except Exception as e:
            print(f"Error saving: {e}")
        return

    print(f"Compressing to target {target_size_mb} MB...")
    
    # Strategy 1: Simple Repack
    try:
        pdf = pikepdf.open(input_file)
        pdf.save(output_file, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
        
        compressed_size = os.path.getsize(output_file)
        compressed_size_mb = compressed_size / (1024 * 1024)
        print(f"Size after repack: {compressed_size_mb:.2f} MB")
        
        if compressed_size_mb <= target_size_mb:
            print("Success with simple repack.")
            return
    except Exception as e:
        print(f"Repack failed: {e}")

    # Strategy 2: Downsample Images
    print("Repack insufficient. Attempting image compression...")
    try:
        pdf = pikepdf.open(input_file) # Re-open to ensure clean state
        
        total_images = 0
        compressed_images = 0
        
        for page in pdf.pages:
            # Get images from resources
            if "/XObject" in page.Resources:
                xobjects = page.Resources.XObject
                for name, xobj in xobjects.items():
                    if xobj.get("/Subtype") == "/Image":
                        total_images += 1
                        # Try to compress
                        compressed_data = compress_image(xobj, quality=40) # Aggressive compression
                        
                        if compressed_data:
                            # Create new stream
                            new_image = pikepdf.Stream(pdf, compressed_data)
                            
                            # Copy metadata
                            for k, v in xobj.items():
                                if k not in ("/Length", "/Filter", "/ColorSpace", "/DecodeParms", "/BitsPerComponent"):
                                    new_image[k] = v
                            
                            # Set new properties
                            new_image.Filter = pikepdf.Name("/DCTDecode")
                            new_image.ColorSpace = pikepdf.Name("/DeviceRGB")
                            new_image.BitsPerComponent = 8
                            
                            # Replace in page resources
                            xobjects[name] = new_image
                            compressed_images += 1

        print(f"Processed {compressed_images}/{total_images} images.")
        
        pdf.save(output_file, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
        
        final_size = os.path.getsize(output_file)
        final_size_mb = final_size / (1024 * 1024)
        print(f"Final Size: {final_size_mb:.2f} MB")
        
        if final_size_mb <= target_size_mb:
            print("Success!")
        else:
            print("Warning: Could not reach target size even with image compression.")
            
    except Exception as e:
        print(f"Image compression failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        input_path = "/Users/lakshmanraghu/Downloads/Medical Expenses part 5.pdf"
        output_path = "/Users/lakshmanraghu/Downloads/Medical Expenses part 5_compressed.pdf"
        print(f"No arguments provided. Using default file: {input_path}")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        
    compress_pdf(input_path, output_path, target_size_mb=14)
