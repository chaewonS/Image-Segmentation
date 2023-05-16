import json
import numpy as np
from PIL import Image

# indexed color mask image 
f = './frankfurt_000001_009504_leftImg8bit_all_objects.png'
originalFormat = np.array(Image.open(f))
height, width = originalFormat.shape[:2]
newImage = np.zeros((height, width), dtype=np.uint16) 

# 픽셀값 배열 바꾸기
for i in range(height):
    for j in range(width):
        if originalFormat[i][j] == 34:
            newImage[i][j] = 0
        else:
            newImage[i][j] = originalFormat[i][j] - 1

# 넘파이 배열을 이미지로 변환
img = Image.fromarray(newImage)
file_path = "./frankfurt_000001_009504_gtFine_instanceIds_check.png"
img.save(file_path)

# 변환한 이미지를 json으로 만들어서 확인
originalFormat2 = np.array(Image.open(file_path))
json_path = "./test.json"
lst = originalFormat2.tolist()

with open(json_path, 'w', encoding='utf-8') as file:
    json.dump(lst, file)