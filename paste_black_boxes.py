
import os
from PIL import Image, ImageDraw


SCREENSHOT_FOLDER = "C:/Users/eMoney/Pictures/Screenshots/Horror_Movies_2022/"
OUTPUT_FOLDER = "C:/Users/eMoney/Pictures/Screenshots/Horror_Movies_2022/Output/"
BLACK = (0, 0, 0)


os.chdir(SCREENSHOT_FOLDER)

# Create list of all files in dir
files = [f for f in os.listdir() if os.path.isfile(f)]

for file in files:

    # print(file)
    filename = SCREENSHOT_FOLDER + file

    with Image.open(file) as im:

        # Copy
        new_image = im.copy()

        # Draw
        draw = ImageDraw.Draw(new_image)
        draw.rectangle(((0.0, 0.0), (1920.0, 120.0)), fill=BLACK)
        draw.rectangle(((0.0, 960.0), (1920.0, 1080.0)), fill=BLACK)

        # Save
        new_filename = OUTPUT_FOLDER + file
        new_image.save(new_filename, "PNG")

