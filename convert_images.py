import os
from PIL import Image
import argparse


def convert_images(input_dir, output_dir, input_format, output_format, include_subfolders, delete_original):
    """
    Converts images from one format to another with optional subfolder processing and deletion of original files.

    Args:
        input_dir (str): Directory containing input images.
        output_dir (str): Directory to save converted images.
        input_format (str): Format of the input images (e.g., 'tif', 'bmp').
        output_format (str): Desired output format (e.g., 'jpeg', 'png').
        include_subfolders (bool): Whether to process subfolders.
        delete_original (bool): Whether to delete original files after conversion.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Walk through the directory (and subdirectories if enabled)
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(f".{input_format.lower()}"):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir) if include_subfolders else ""
                save_dir = os.path.join(output_dir, relative_path)

                # Create output subfolder if necessary
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                output_path = os.path.join(save_dir, os.path.splitext(file)[0] + f".{output_format.lower()}")

                try:
                    # Convert and save the image
                    with Image.open(input_path) as img:
                        print(f"Converting: {input_path} -> {output_path}")
                        img = img.convert("RGB")
                        img.save(output_path, output_format.upper(), quality=90)

                    # Delete the original file if specified
                    if delete_original:
                        os.remove(input_path)
                        print(f"Deleted original file: {input_path}")

                except Exception as e:
                    print(f"Error processing file {input_path}: {e}")

        # Skip subfolders if not included
        if not include_subfolders:
            break


if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert images between formats.")
    parser.add_argument("--input_dir", type=str, required=True, help="Directory containing input images.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save converted images.")
    parser.add_argument("--input_format", type=str, required=True, help="Format of input images (e.g., tif, bmp).")
    parser.add_argument("--output_format", type=str, required=True, help="Format of output images (e.g., jpeg, png).")
    parser.add_argument("--include_subfolders", action="store_true", help="Process subfolders recursively.")
    parser.add_argument("--delete_original", action="store_true", help="Delete original files after conversion.")

    args = parser.parse_args()

    convert_images(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        input_format=args.input_format,
        output_format=args.output_format,
        include_subfolders=args.include_subfolders,
        delete_original=args.delete_original,
    )
