# gtFine_color.png 생성
# 투명도 포함, 파일 이름 변경
import numpy as np
from PIL import Image
import os
from multiprocessing import Pool

def process_image(filename):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder_path, filename))

        # 이미지 크기 조정
        width, height = image.size
        target_size = (width, height)

        # 이미지를 RGBA 형식의 배열로 변환
        image_rgba = image.convert('RGBA')
        image_array = np.array(image_rgba)

        # 투명도 값 설정
        alpha_value = 255

        # 각 픽셀에 투명도 값 할당
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                image_array[i, j, 3] = alpha_value

        # RGBA 배열을 이미지로 변환
        file_parts = filename.split("_")
        file_name = f"{file_parts[0]}_{file_parts[1]}_gtFine_color.png"
        result_image = Image.fromarray(image_array)
        result_image = result_image.resize(target_size)
        output_filepath = os.path.join(output_folder, file_name)
        result_image.save(output_filepath)

folder_path = "/home/ubuntu/cw/OneFormer/input/Screenshots/*"
all_file = set(os.listdir(folder_path))
output_folder = "/home/ubuntu/cw/OneFormer/output/Color/*"

# multiprocessing을 사용하여 병렬 처리
pool = Pool()
pool.map(process_image, all_file)
pool.close()
pool.join()
