import sys
import os
from PIL import Image

# grab 1st and 2nd argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exists, if not creat a new ting
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through pokedex

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename) [0]
	print(clean_name)
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print("all done!")

