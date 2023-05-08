from PIL import Image
import os

# 이미지 경로 지정
image_folder = "./0508_TEST_masked"
output_folder = "image_processed/"
os.makedirs(output_folder, exist_ok=True)

# 출력되는 전체 이미지에 대해 합성
# foreground 이미지가 여러 개인 경우, 리스트를 생성 필요
images = []
# id가 같은 이미지끼리 묶어서 이미지 합성 (딕셔너리 생성)
image_field = {}

# 폴더 내 이미지 파일 하나씩 처리
for filename in os.listdir(image_folder):
    if filename.endswith(".png"):
        input_filepath = os.path.join(image_folder, filename)
        class_name = filename.split("_")[-1][:-4]
        image_id = filename.split("_")[2]
        check = ["car", "truck", "train", "person", "bus", "rider", "bicycle", "motorcycle"]

        if class_name in check:
            if image_id in image_field:
                image_field[image_id].append(Image.open(input_filepath))
            else:
                image_field[image_id] = [Image.open(input_filepath)]

            if len(image_field[image_id]) > 1:
                # 현재 첫 번째 이미지를 background로 설정
                background = image_field[image_id][0]
                # 나머지 이미지를 forground로 설정
                for foreground in image_field[image_id][1:]:
                    # 이미지 합성
                    background.paste(foreground, (0,0), foreground)

                # 저장할 이미지 이름 생성
                file_parts = filename.split("_")
                file_name = f"{file_parts[0]}_{file_parts[1]}_{file_parts[2]}_2.png"
                output_filepath = os.path.join(output_folder, file_name)
                # 최종 이미지 저장
                background.save(output_filepath)
