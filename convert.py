import os
import numpy as np
from PIL import Image
from tqdm import tqdm
from pdf2image import convert_from_path
import img2pdf

input_folder = '/home/zhaozhiyou/input'
output_folder = '/home/zhaozhiyou/output'
input_ = '/home/zhaozhiyou/origin.pdf'
output = '/home/zhaozhiyou/new.pdf'

def conv_single(img):
    array = np.array(img)
    size = array.shape

    array = array.reshape((-1, 3))
    mask = (array[:, 0] > 160)
    array[mask] = [255,255,255]
    return Image.fromarray(array.reshape(size))

convert_from_path(input_, fmt='png', size=(3000, None), output_folder=input_folder)

images = os.listdir(input_folder)
images.sort()
for i, image in tqdm(enumerate(images)):
    img = Image.open(os.path.join(input_folder, image))
    img = conv_single(img)
    img.save(os.path.join(output_folder, str(i) + '.png'))

images = os.listdir(output_folder)
images.sort(key=lambda x: int(x[:-4]))
os.chdir(output_folder)
with open(output, "wb") as f:
    f.write(img2pdf.convert(images))
