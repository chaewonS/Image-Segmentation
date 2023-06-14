import sys
import json
import numpy as np
from PIL import Image, ImageDraw
from pycocotools import mask as maskUtils
import os
import shutil
import multiprocessing

# python instanceIds.py 0601 CW
# 입력 인수 가져오기
if len(sys.argv) != 3:
    print("사용법: python test.py <이미지 폴더 경로> <JSON 파일 경로>")
    sys.exit(1)

argv1 = sys.argv[1]
argv2 = sys.argv[2]
img_dir = f"/home/ubuntu/cw/OneFormer/input/All_objects/{argv1}/{argv2}"
json_path = f"/home/ubuntu/cw/OneFormer/input/RectLabel_coco/coco_{argv2}.json"
new_img_dir = f"/home/ubuntu/cw/OneFormer/output/InstanceIds/{argv1}"

# 이미지 폴더 생성 또는 이미지 삭제
if os.path.exists(new_img_dir):
    shutil.rmtree(new_img_dir)
os.makedirs(new_img_dir)

# 다중 프로세싱을 사용하여 작업 병렬화
# multiprocessing 모듈을 사용하여 이미지 처리 작업을 여러 개의 프로세스로 분할하여 실행 (작업 시간 단축)
def process_image(img_path, img_id, obj_list, label_dict):
    mask = np.array(Image.open(img_path))
    height, width = mask.shape[:2]
    newImage = np.array(mask, dtype=np.uint16)

    for obj in obj_list:
        rle = obj['segmentation']
        mask = maskUtils.decode(rle)

        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if mask[i, j] == 1:
                    newImage[i][j] = label_dict[obj['id']]

    img_filename = os.path.splitext(os.path.basename(img_path))[0]
    new_img_filename = img_filename.replace("_all_objects", "_gtFine_instanceIds") + ".png"

    output_path = os.path.join(new_img_dir, new_img_filename)
    Image.fromarray(newImage).save(output_path)


# JSON 파일 읽기
with open(json_path, 'r') as f:
    data = json.load(f)

# 이미지 처리 작업 병렬화를 위한 프로세스 개수 설정
num_processes = multiprocessing.cpu_count()

# 이미지 처리 작업을 병렬로 실행
pool = multiprocessing.Pool(processes=num_processes)
for img in data['images']:
    img_filename = img['file_name']
    mask_name = img_filename.replace(".jpg", "_all_objects.png")
    img_path = os.path.join(img_dir, mask_name)

    obj_list = sorted(
        [
            obj
            for obj in data['annotations']
            if obj['category_id'] in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36] and obj['image_id'] == img['id']
        ],
        key=lambda obj: obj['id']
    )

    label_dict = {}

    for category_id in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36]:
        obj_list_category = [obj for obj in obj_list if obj['category_id'] == category_id]
        label_count = 0

        for obj in obj_list_category:
            if obj['id'] not in label_dict:
                label_dict[obj['id']] = category_id * 1000 + label_count
                label_count += 1
    pool.apply_async(process_image, args=(img_path, img['id'], obj_list, label_dict))
pool.close()
pool.join()
f.close()
