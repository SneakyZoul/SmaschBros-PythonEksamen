import PIL
from PIL import Image
import numpy as np
from PIL import Image
import os
from os import listdir

from config.definitions import ROOT_DIR


def get_images(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    all_pixel_values = []

    for image_file_name in os.listdir(image_path):
        print(image_file_name)
        image_ = Image.open(image_path+"/" + image_file_name, "r")
        width, height = image_.size
        pixel_values = list(image_.getdata())
        if image_.mode == "RGB":
            channels = 3
        elif image_.mode == "L":
            channels = 1
        else:
            print("Unknown mode: %s" % image_.mode)
            return None
        """Make the matix 3 an 3D array"""
        pixel_values = np.array(pixel_values).reshape((width, height, channels))
        """Makes the matix 4 an 4D array"""
        p = np.array([pixel_values])
        all_pixel_values.append((image_file_name.split("_")[0],p))
    return all_pixel_values


if __name__ == '__main__':
    image_array_pixel_value= get_images(os.path.join(ROOT_DIR, 'data', 'resizedImages'))

    print("Here is value",image_array_pixel_value)

