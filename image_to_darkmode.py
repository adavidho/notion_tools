#!/usr/bin/env python

from PIL import Image, ImageGrab, ImageOps
import subprocess
import argparse
from PIL import Image
import io
import pasteboard


def invert_image_colors(image):
    # Invert image colors
    # inverted_image = Image.eval(image, lambda px: 255 - px)
    inverted_image = ImageOps.invert(image)
    # Replace background color with #191919
    width, height = image.size
    background_color = (25, 25, 25)  # RGB value for #191919
    tolerance = 20
    for x in range(width):
        for y in range(height):
            if all(
                abs(p - 0) <= tolerance
                for p in inverted_image.getpixel((x, y))
            ):
                inverted_image.putpixel((x, y), background_color)

    return inverted_image


def save_image_to_clipboard(image):
    pb = pasteboard.Pasteboard()
    data_bytes = io.BytesIO()
    image.save(data_bytes, format="JPEG", quality=90)
    data_bytes = data_bytes.getvalue()
    pb.set_contents(data=data_bytes, type=pasteboard.TIFF)
    print("Converted clipboard image to JPG.")
    # Save the image to a temporary file
    # temp_filename = "/tmp/temp_image.png"
    # image.save(temp_filename)

    # # Use pbcopy to copy the contents of the temporary file to the clipboard
    # subprocess.run(
    #     ["pbcopy"], input=open(temp_filename, "rb").read(), check=True
    # )

    print("Image copied to clipboard")


def main(file_name):
    # Open image file
    if file_name:
        image = Image.open(file_name)
        print("Load file")
    else:
        image = ImageGrab.grabclipboard()
        print("Load from clipboard")
    print(image)
    # Invert image colors and replace background color
    inverted_image = invert_image_colors(image.convert("RGB"))

    # Save the result
    if file_name:
        inverted_image.save("notion_" + file_name)
    save_image_to_clipboard(inverted_image)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Invert image colors and replace background color"
    )
    parser.add_argument(
        "file_name",
        nargs="?",
        default=None,
        type=str,
        help="Name of the image file",
    )
    args = parser.parse_args()

    main(args.file_name)
