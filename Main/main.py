import sys
import json
import numpy as np
from PIL import Image, ImageDraw
from pycocotools import mask as maskUtils
import os
import shutil
from multiprocessing import Pool
import glob

# python main.py 0601
def rename_and_move(all_objects_folder, labelIds_folder):
    search_string = "*_all_objects.png"

    if not os.path.exists(labelIds_folder):
        os.makedirs(labelIds_folder)
    else:
        shutil.rmtree(labelIds_folder)
        os.makedirs(labelIds_folder)

    for file_path in glob.glob(os.path.join(all_objects_folder, search_string)):
        mask = np.array(Image.open(file_path), dtype=np.uint16)
        mask = np.where((mask >= 1) & (mask <= 38), mask - 1, mask)
        new_file_name = os.path.basename(file_path).replace("_leftImg8bit_all_objects.png", "_gtFine_labelIds.png")
        new_file_path = os.path.join(labelIds_folder, new_file_name)
        Image.fromarray(mask).save(new_file_path)


def create_Color(filename):
    if filename.endswith(".jpg"):
        image = Image.open(os.path.join(color_img_dir, filename))

        width, height = image.size
        target_size = (width, height)

        image_rgba = image.convert('RGBA')
        image_array = np.array(image_rgba)

        alpha_value = 255

        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                image_array[i, j, 3] = alpha_value

        # file_parts = filename.split("_")
        # file_name = f"{file_parts[0]}_{file_parts[1]}_{file_parts[2]}_{file_parts[3]}_gtFine_color.png"
        file_name = filename.replace("_leftImg8bit.jpg", "_gtFine_color.png")
        result_image = Image.fromarray(image_array).resize(target_size)
        output_filepath = os.path.join(color_new_img_dir, file_name)
        result_image.save(output_filepath)

def create_Polygon(labelme_folder, polygon_folder):
    for filename in os.listdir(labelme_folder):
        if filename.endswith(".json"):
            input_filepath = os.path.join(labelme_folder, filename)
            with open(input_filepath, "r") as f:
                data = json.load(f)

                objects = []
                num_instances = len(data['shapes'])

                for i in range(num_instances):
                    object_field = {
                        'label' : data['shapes'][i]['label'],
                        'polygon' : data['shapes'][i]['points']
                    }
                    objects.append(object_field)

                fcn_dict = {}
                fcn_dict['imgHeight'] = data['imageHeight']
                fcn_dict['imgWidth'] = data['imageWidth']
                fcn_dict['objects'] = objects

                # name, ext = filename.split('.')
                # output_filename = name + "_gtFine_polygons" + "." + ext
                output_filename = filename.replace("_leftImg8bit.json", "") + "_gtFine_polygons.json"
                output_filepath = os.path.join(polygon_folder, output_filename)

                with open(output_filepath, "w", encoding="utf-8") as fo:
                    json.dump(fcn_dict, fo)

def Check_Error_Polygon(polygon_folder):
    all_filenames = set(os.listdir(polygon_folder))

    for filename in all_filenames:
        if filename.endswith(".json"):
            file_path = os.path.join(polygon_folder, filename)

            with open(file_path, "r") as f:
                data = json.load(f)

            modified_objcts = []
            for obj in data['objects']:
                try:
                    polygon = obj['polygon']
                    if isinstance(polygon, list) and len(polygon) >= 2:
                        modified_objcts.append(obj)
                    else:
                        print(f"{filename}: {obj['label']} polygon is invalid.")
                except KeyError:
                    print(f"{filename}: No polygon found for {obj['label']}.")
                except TypeError:
                    print(f"{filename}: Invalid polygon for {obj['label']}.")
            data['objects'] = modified_objcts

            with open(file_path, 'w') as f:
                json.dump(data, f)

            print(f"Modified file: {filename}")
    for filename in os.listdir(polygon_folder):
        if filename.endswith(".json"):
            if filename not in all_filenames:
                print(f"Missing file: {filename}")

if __name__ == "__main__":
    # python main.py 0601
    if len(sys.argv) != 2:
        print("사용법: python main.py <이미지 폴더 경로>")
        sys.exit(1)

    argv1 = sys.argv[1]
    # Create Color
    color_img_dir = f"/home/ubuntu/cw/OneFormer/input/Screenshots/{argv1}"
    color_new_img_dir = f"/home/ubuntu/cw/OneFormer/output/Color/{argv1}"
    all_file = set(os.listdir(color_img_dir))
    # Create LabelIds
    all_objects_dir = f"/home/ubuntu/cw/OneFormer/input/All_objects/{argv1}"
    labelIds_dir = f"/home/ubuntu/cw/OneFormer/output/LabelIds/{argv1}"
    # Create Polygon
    labelme_dir = f"/home/ubuntu/cw/OneFormer/input/Labelme/{argv1}"
    polygon_dir = f"/home/ubuntu/cw/OneFormer/output/Polygon/{argv1}"

    os.makedirs(polygon_dir, exist_ok=True)
    img_files = os.listdir(labelme_dir)
    img_files.sort()

    if os.path.exists(color_new_img_dir):
        shutil.rmtree(color_new_img_dir)
    os.makedirs(color_new_img_dir)

    rename_and_move(all_objects_dir, labelIds_dir)
    create_Polygon(labelme_dir, polygon_dir)
    Check_Error_Polygon(polygon_dir)

    pool = Pool()
    pool.map(create_Color, all_file)
    pool.close()
    pool.join()
