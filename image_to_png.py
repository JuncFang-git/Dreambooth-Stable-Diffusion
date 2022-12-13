import os
import PIL.Image as Image
from tqdm import tqdm

SRC_DIR = "/home/junkai/data/dreambooth/sam-512"
DEST_DIR = "/home/junkai/data/dreambooth/sam-512"

image_list = os.listdir(SRC_DIR)
for img_name in tqdm(image_list):
    if img_name.endswith(".png"):
        continue
    src_img_path = os.path.join(SRC_DIR, img_name)
    dst_name = img_name.split(".")[0] + ".png"
    dst_img_path = os.path.join(DEST_DIR, dst_name)
    # print(dst_img_path) # for debug print
    
    img = Image.open(src_img_path)
    img.save(dst_img_path)
    os.remove(src_img_path)
