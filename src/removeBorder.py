#! python3
# Goes through all the .png and .jpg images in the current working directory and removes any solid-colored border from the sides.

import os
from PIL import Image

# columnIsSameColor() checks if an entire column is a single color.
def columnIsSameColor(im, x):
    # Return True if column x in im is all the same color.
    color = im.getpixel((x, 0))
    for y in range(im.size[1]): # loop over all columns
        if im.getpixel((x,y)) != color:
            return False
    return True

# rowIsSameColor() to check if an entire row is a single color.
def rowIsSameColor(im, y):
    # Return True if row y in im is all the same color.
    color = im.getpixel((0, y))
    for x in range(im.size[0]): # loop over all rows
        if im.getpixel((x,y)) != color:
            return False
    return True

# Loop through all the files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue # skip this non-image file

    currentIm = Image.open(filename)
    width, height = currentIm.size

    # Find left side border.
    for left in range(width):
        if not columnIsSameColor(currentIm, left):
            break

    # Find right side border.
    for right in range(width - 1, -1, -1):
        if not columnIsSameColor(currentIm, right):
            break

    # Find top side border.
    for top in range(height):
        if not rowIsSameColor(currentIm, top):
            break

    # Find bottom side border.
    for bottom in range(height - 1, -1, -1):
        if not rowIsSameColor(currentIm, bottom):
            break

    # Check if there were any borders.
    if left == 0 and right == width - 1 and top == 0 and bottom == height - 1:
        print('Skipping %s...' % (filename))
        continue # no border, skip this image

    # Remove the borders.
    print('Removing border from %s...' % (filename))
    currentIm = currentIm.crop((left + 1, top + 1, right, bottom))
    currentIm.save(filename)
