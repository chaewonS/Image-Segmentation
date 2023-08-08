import os
import sys

if len(sys.argv) != 2:
    print("사용법: rename.py <날짜>")
    sys.exit(1)

argv1 = sys.argv[1]
folder_path = f"/home/ubuntu/cw/OneFormer/input/Seo_rename/{argv1}"

for subfolder_name in os.listdir(folder_path):
    # 입력 argv1 값을 기반으로, 해당 폴더 내부의 서브 폴더들 검사
    # 폴더명에 따라 파일 이름 변경
    subfolder_path = os.path.join(folder_path, subfolder_name)

    if os.path.isdir(subfolder_path):
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)

            # 이미지 파일 이름에 'image'를 발견하면 'iimage'로 변경
            if 'image' in filename:
                new_filename = filename.replace('image', 'iimage')
                new_file_path = os.path.join(subfolder_path, new_filename)
                if os.path.exists(file_path) and not os.path.exists(new_file_path):
                    os.rename(file_path, new_file_path)
            
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)

            if filename.endswith(".png"):
                if subfolder_name == "Color":
                    new_filename = filename.replace("_leftImg8bit.png", "_gtFine_color.png")
                elif subfolder_name == "InstanceIds":
                    new_filename = filename.replace("_leftImg8bit.png", "_gtFine_instanceIds.png")
                elif subfolder_name == "LabelIds":
                    new_filename = filename.replace("_leftImg8bit.png", "_gtFine_labelIds.png")
                else:
                    continue  # 이미 변경된 경우, 이름 변경을 수행하지 않음
                os.rename(file_path, os.path.join(subfolder_path, new_filename))

            elif filename.endswith(".json"):
                if subfolder_name == "Polygon":
                    new_filename = filename.replace("_leftImg8bit.json", "_gtFine_polygons.json")
                    os.rename(file_path, os.path.join(subfolder_path, new_filename))
