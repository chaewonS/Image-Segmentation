# gtFine_polygons.josn 생성
# polygons 에러 수정

import os
import json

folder_path = "/home/ubuntu/cw/OneFormer/output/Polygon/*"
all_filenames = set(os.listdir(folder_path))

for filename in all_filenames:
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r') as f:
            data = json.load(f)

        modified_objects = []
        for obj in data['objects']:
            try:
                polygon = obj['polygon']
                if isinstance(polygon, list) and len(polygon) >= 2:
                    modified_objects.append(obj)
                else:
                    print(f"{filename}: {obj['label']} polygon is invalid.")
            except KeyError:
                print(f"{filename}: No polygon found for {obj['label']}.")
            except TypeError:
                print(f"{filename}: Invalid polygon for {obj['label']}.")

        data['objects'] = modified_objects

        with open(file_path, 'w') as f:
            json.dump(data, f)

        print(f"Modified file: {filename}")

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        if filename not in all_filenames:
            print(f"Missing file: {filename}")
