# Image to Darkmode

This CLI tool can load an image with white background from a file or from the clipboard, inverts its colours and changes the backround to the Notion dark mode colour (#191919). The tool is made to work with the Mac clipboard.

To use this tool, simply clone the repository, add excecutable permissions to the `image_to_darkmode.py` file and copy it into a path directory (such as `/usr/local/bin/` on mac.
Now copy an image to clipboard and the run `image_to_darkmode`. It will pull the image from the clipboard change it and past the updated version back to the clipboard. Alternatively you can specify the name of an image file that will be read in (e.g. `image_to_darkmode my_image.png`). The output image will be both saved as a file and copied to the clipboard.


