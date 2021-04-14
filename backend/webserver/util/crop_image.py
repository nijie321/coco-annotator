from PIL import Image
import os

from database import ImageModel

def crop(path, dataset_id):
    pil_image = Image.open(path)
    
    directory = os.path.dirname(path)
    base_name = os.path.basename(path)
    
    width, height = pil_image.size

    crop_width = width / 2
    crop_height = height / 2

    top_left_box = (0,0, crop_width, crop_height)
    top_right_box = (crop_width, 0, width, crop_height)
    bottom_left_box = (0, crop_height, crop_width, height)
    bottom_right_box = (crop_width, crop_height, width, height)

    file_names = [os.path.join(directory, f"{base_name}_{f_name}") \
        for f_name in ["topleft.png", "topright.png", "bottomleft.png", "bottomright.png"]]

    # pil_image.crop(top_left_box).save(os.path.join(directory, f"{base_name}_topleft.png"))
    # pil_image.crop(top_right_box).save(os.path.join(directory, f"{base_name}_topright.png"))
    # pil_image.crop(bottom_left_box).save(os.path.join(directory, f"{base_name}_bottomleft.png"))
    # pil_image.crop(bottom_right_box).save(os.path.join(directory, f"{base_name}_bottomright.png"))

    pil_image.crop(top_left_box).save(file_names[0])
    pil_image.crop(top_right_box).save(file_names[1])
    pil_image.crop(bottom_left_box).save(file_names[2])
    pil_image.crop(bottom_right_box).save(file_names[3])
    
    for fn in file_names:
        ImageModel.create_from_path(fn, dataset_id).save()