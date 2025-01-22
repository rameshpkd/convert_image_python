# convert_image_python

## Overview

This repository contains two Python scripts designed for batch image conversion:

1. **`convert_images.py`**: A command-line interface (CLI) tool that converts images from one format to another using command-line arguments.
2. **`convert_images_interactive.py`**: An interactive version of the script that prompts the user for input during execution.

Both scripts utilize the Python Imaging Library (PIL) to perform the conversions.

## Features

- **Batch Conversion**: Convert multiple images in a directory to a specified format.
- **Subfolder Processing**: Option to include subfolders in the conversion process.
- **Original File Deletion**: Option to delete original files after successful conversion.

## Prerequisites

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/) library

## Installation (optional, copy the code and run in your python environment)

1. Clone the repository:

   ```bash
   git clone https://github.com/rameshpkd/convert_image_python.git
   cd convert_image_python

2. Install the required dependencies:

pip install -r requirements.txt



Usage

convert_images.py (CLI Version)

This script converts images from one format to another using command-line arguments.

Command-Line Arguments:
• --input_dir: Directory containing input images. Default is ./input.
• --output_dir: Directory to save converted images. Default is ./output.
• --input_format: Format of input images (e.g., tif, bmp). Default is tif.
• --output_format: Format of output images (e.g., jpeg, png). Default is jpeg.
• --include_subfolders: Process subfolders recursively.
• --delete_original: Delete original files after conversion.

Example Usage:

python convert_images.py --input_dir ./input --output_dir ./output --input_format tif --output_format jpeg --include_subfolders --delete_original

convert_images_interactive.py (Interactive Version)

This script prompts the user for input during execution.

Usage:
1. Run the script:

python convert_images_interactive.py


2. The script will prompt you for the following inputs:
• Input directory (default: ./input)
• Output directory (default: ./output)
• Input image format (default: tif)
• Output image format (default: jpeg)
• Include subfolders? (yes/no)
• Delete original files after conversion? (yes/no)

4. After providing the required information, the script will proceed to convert the images as specified.

License

Acknowledgments
• Pillow Documentation
• Python argparse Module

