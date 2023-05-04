from PIL import Image
import os

# 이미지 경로 지정
image_folder = "./"
output_folder = "image_processed/"
os.makedirs(output_folder, exist_ok=True)

# 출력되는 전체 이미지에 대해 합성
# foreground 이미지가 여러 개인 경우, 리스트를 생성 필요
images = []
# 폴더 내 이미지 파일 하나씩 처리
for filename in os.listdir(image_folder):
    if filename.endswith(".png"):
        input_filepath = os.path.join(image_folder, filename)
        class_name = filename.split("_")[-1][:-4]
        check = ["car", "truck", "train", "person", "bus", "rider", "bicycle", "motorcycle"]
    
        if class_name in check:
            img = Image.open(input_filepath)
            # 리스트에 이미지 추가
            images.append(img)

# 리스트에 있는 모든 이미지 합성
if len(images) > 0:
    # 현재 첫 번째 이미지를 background로 설정
    background = images[0]
    # 나머지 이미지를 forground로 설정
    for foreground in images[1:]:
        # 이미지 합성
        background.paste(foreground, (0,0), foreground)
    # 저장할 이미지 이름 생성
    file_parts = filename.split("_")
    file_name = f"{file_parts[0]}_{file_parts[1]}_{file_parts[2]}.png"
    output_filepath = os.path.join(output_folder, file_name)
    # 최종 이미지 저장
    background.save(output_filepath)
