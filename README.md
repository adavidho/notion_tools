# Image to Darkmode

This CLI tool can load an image with white background from a file or from the clipboard, inverts its colours and changes the backround to the Notion dark mode colour (#191919). The tool is made to work with the Mac clipboard.

## How to Setup
1. Clone the repository
2. Add excecutable permissions to the `image_to_darkmode.py` file with `chmod +x image_to_darkmode.py`
3. Copy the file into a path directory (e.g as `sudo cp image_to_darkmode.py /usr/local/bin/image_to_darkmode`)

## How to Use
The tool can be used in two ways. Either it reads a file from the working directory or it loads the image from the clipboard. In the former case specify the name of an image file that will be read in (e.g. `image_to_darkmode my_image.png`). The output image will be both saved as a file and copied to the clipboard.

In the second case, simply copy an image to clipboard and then run `image_to_darkmode` comand. It will pull the image from the clipboard change it and past the updated version back to the clipboard. 

## Example
1. Make a screen shot and copy it to the clipboard with <kbd>⇧</kbd>+<kbd>⌃</kbd>+<kbd>⌘</kbd>+<kbd>4</kbd>. For example this image of a gaussian distribution: <img width="588" alt="image" src="https://github.com/adavidho/notion_tools/assets/105221763/4c3aee12-6605-41f8-995d-ee42e388153f"> 
2. Run the `image_to_darkmode` comand in the terminal.
3. And paste the result into your notion document using <kbd>⌘</kbd>+<kbd>V</kbd>, as seen with the example image below: <img width="588" alt="image" src="https://github.com/adavidho/notion_tools/assets/105221763/133fde70-f478-4551-b8cc-642368b8d98c">


