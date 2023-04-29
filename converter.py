# python image library
from PIL import Image

import glob

# print current png files
print(glob.glob('*.png'))

for file in glob.glob('*.png'):
    # open image file
    im = Image.open(file)

    # convert to RGB file format
    rgb_im = im.convert('RGB')

    # save jpg file
    rgb_im.save(file.replace('png', 'jpg'), quality=95)
