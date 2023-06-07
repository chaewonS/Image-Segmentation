# gtFine_labelIds.png 생성
# 이름 변경
import glob
import os
import shutil

folder_path = "/home/ubuntu/cw/OneFormer/input/All_objects/*"
search_string = "*_all_objects.png"
output_folder = "/home/ubuntu/cw/OneFormer/output/LabelIds/*"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_path in glob.glob(os.path.join(folder_path, search_string)):
    new_file_name = os.path.basename(file_path).replace("_all_objects.png", "_gtFine_labelIds.png")
    new_file_path = os.path.join(output_folder, new_file_name)
    shutil.move(file_path, new_file_path)

print("이미지 파일 이름 변경 및 이동이 완료되었습니다.")
