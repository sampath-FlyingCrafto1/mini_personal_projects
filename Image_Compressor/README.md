# Image Compression Tool with EasyGUI

This script provides a user-friendly interface to compress image files using Python libraries.

## How it works

1. The code imports necessary libraries:
   - `PIL.Image` for image processing.
   - `os` for file system operations.
   - `easygui` for creating a simple graphical user interface.
2. It defines a function `resizer()` that performs the image compression:
   - It prompts the user to select an image file using `easygui.fileopenbox()`.
   - It retrieves the selected file path.
   - It extracts the filename and extension from the path.
   - It opens the image using `Image.open(filepath)`.
   - Based on the file extension:
     - For JPEG images (".jpeg" or ".jpg"):
       - It prompts the user to enter a compression quality level (10-100) using `easygui.integerbox()`.
       - It saves the compressed image with a "_compressed" suffix using `img.save()`, specifying JPEG format, optimization, and the user-provided quality.
       - It displays a message box indicating successful compression.
     - For PNG images (".png"):
       - It converts the image to a palette-based format for better compression using `img.convert()`.
       - It saves the compressed image with a "_compressed" suffix using `img.save()`, specifying PNG format, optimization, and maximum quality (10).
       - It displays message boxes informing the user about potential limitations of PNG compression and successful compression.
     - For other file types:
       - It prints an error message indicating invalid file type.
3. It calls the `resizer()` function to start the image compression process.

## Running the code

1. Save the code as a Python file (e.g., `image_compressor.py`).
2. Ensure you have the required libraries installed (`PIL`, `easygui`). You can install them using `pip install Pillow easygui`.
3. Open a terminal or command prompt and navigate to the directory where you saved the file.
4. Run the script using the following command:

```bash
python image_compressor.py