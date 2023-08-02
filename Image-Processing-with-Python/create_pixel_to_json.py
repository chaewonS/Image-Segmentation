import os
import glob
import sys
import argparse
import json
import numpy as np

from PIL import Image

# indexed color mask image -> json으로 체크
f = './TEST/230622_1/230622_1_image_raw2_gtFine_instanceIds.png'

originalFormat = np.array(Image.open(f))
file_path = "./TEST.json"
lst = originalFormat.tolist()

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(lst, file)
