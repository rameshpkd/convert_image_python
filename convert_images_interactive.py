import os
from PIL import Image

def get_user_input(prompt, default=None):
    user_input = input(f"{prompt} [{default}]: ") or default
    return user_input

def convert_images(input_dir, output_dir, input_format, output_format, include_subfolders, delete_original):
    # Ensure input and output directories exist
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine the appropriate function to traverse directories
    if include_subfolders:
        walker = os.walk(input_dir)
    else:
        walker = [(input_dir, [], os.listdir(input_dir))]

    for root, _, files in walker:
        for filename in files:
            if filename.lower().endswith(f".{input_format.lower()}"):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)
                output_filename = f"{os.path.splitext(filename)[0]}.{output_format.lower()}"
                output_path = os.path.join(output_subdir, output_filename)

                try:
                    with Image.open(input_path) as img:
                        rgb_img = img.convert("RGB")
                        rgb_img.save(output_path, output_format.upper())
                    print(f"Converted '{input_path}' to '{output_path}'")
                    if delete_original:
                        os.remove(input_path)
                        print(f"Deleted original file '{input_path}'")
                except Exception as e:
                    print(f"Failed to convert '{input_path}': {e}")

if __name__ == "__main__":
    print("Welcome to the Image Converter Script!")

    # Prompt user for inputs
    input_dir = get_user_input("Enter the input directory", "./input")
    output_dir = get_user_input("Enter the output directory", "./output")
    input_format = get_user_input("Enter the input image format (e.g., tif, bmp)", "tif")
    output_format = get_user_input("Enter the output image format (e.g., jpeg, png)", "jpeg")
    include_subfolders = get_user_input("Include subfolders? (yes/no)", "no").lower() == 'yes'
    delete_original = get_user_input("Delete original files after conversion? (yes/no)", "no").lower() == 'yes'

    # Run the conversion process
    convert_images(input_dir, output_dir, input_format, output_format, include_subfolders, delete_original)
    print("Image conversion process completed.")
