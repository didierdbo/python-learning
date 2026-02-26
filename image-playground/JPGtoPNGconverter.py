import sys
import os
from PIL import Image

# grab the first and second argument
src_dir = sys.argv[1]
dst_dir = sys.argv[2]

# check if new/ exists, if not create
if not os.path.isdir(dst_dir):
    os.makedirs(dst_dir)

# loop through Pokedex,
# convert images to png
# save to the new folder.
directory = os.fsencode(src_dir)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img = Image.open(f"{src_dir}{filename}")
    dst_filename = os.path.splitext(filename)[0] + ".png"
    img.save(f"{dst_dir}{dst_filename}", "png")
