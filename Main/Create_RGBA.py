from PIL import Image, ImageDraw
import json
import os
import numpy as np
import sys

if len(sys.argv) != 2:
    print("사용법: python test.py <Polygon 폴더 경로>")
    sys.exit(1)

argv1 = sys.argv[1]
# 입력 데이터 (폴리곤 정보를 담은 JSON 데이터)
folder_path = f"/home/ubuntu/cw/OneFormer/output/Polygon/{argv1}"
output_folder = f"/home/ubuntu/cw/OneFormer/output/Color/{argv1}"
all_filenames = set(os.listdir(folder_path))

# 색상 매핑 (각 라벨에 대한 RGB 값)
color_mapping = {
    "unlabeled": [0, 0, 0],
    "road": [128, 64, 128],
    "sidewalk": [244, 35, 232],
    "building": [70, 70, 70],
    "wall": [102, 102, 156],
    "fence": [190, 153, 153],
    "pole": [153, 153, 153],
    "traffic sign": [220, 220, 0],
    "vegetation": [107, 142, 35],
    "terrain": [152, 251, 152],
    "sky": [70, 130, 180],
    "person": [220, 20, 60],
    "car": [0, 0, 142],
    "truck": [0, 0, 70],
    "huge truck": [13, 208, 131],
    "gas storage": [170, 60, 10],
    "hazard storage": [230, 180, 70]
}

for filename in all_filenames:
    if filename.endswith("polygons.json"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r') as f:
            data = json.load(f)

        # 새로운 이미지 생성
        image = Image.new("RGB", (data["imgWidth"], data["imgHeight"]), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        # JSON 객체를 반복하여 폴리곤 정보를 가져와 색상을 적용
        for obj in data["objects"]:
            label = obj["label"]
            polygon = [(point[0], point[1]) for point in obj["polygon"]]
            color = tuple(color_mapping.get(label, [0, 0, 0]))  # 라벨에 해당하는 색상 또는 검정색

            draw.polygon(polygon, fill=color)

        # RGBA 이미지 생성 (alpha 값은 255)
        rgba_image = image.convert("RGBA")
        r, g, b, _ = rgba_image.split()
        rgba_image = Image.merge("RGBA", (r, g, b, Image.new("L", rgba_image.size, 255)))

        # 이미지 저장
        output_filename = filename.replace("_polygons.json", "_color.png")
        output_path = os.path.join(output_folder, output_filename)
        rgba_image.save(output_path)

        print(f"Processed: {filename} -> {output_filename}")
