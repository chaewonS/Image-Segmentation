# KETI Project1 (3/9~)
# Image-Segmentation, Auto Labeling
for Autonomous Driving and Real-time Object Detection
![Image_segmentation_process](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/40411106-c5f4-4be4-a15d-a0a3080b1845)

## OneFormer: One Transformer to Rule Universal Image Segmentation
### Panoptic Segmentation on Cityscapes
![keti1](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/28494afb-8720-495f-82b9-f6c5c01896d8)
![keti2](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/21ac4c95-80cf-416a-9262-9fd41385f48d)
![keti3](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/c732ec8a-9580-4eb9-a106-b82686bb6cf0)

#### Use RectLabel(macOS) Segmentation Tool

![image](https://user-images.githubusercontent.com/81732426/228161115-16d28e8b-4570-4a09-bbea-b114960ad627.png)
#### Oneformer panoptic task ouput image

___
## Install
### CUDA 11.1 + Torch 1.9
``` pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html ```

### Install detectron2
``` https://dl.fbaipublicfiles.com/detectron2/wheels/cu111/torch1.9/index.html ```

### Install natten
``` pip3 install natten==0.14.2 -f https://shi-labs.com/natten/wheels/cu111/torch1.9/index.html ```
___

**구현 완료**
+ Pre-segmentation using SOTA
  + detectron2, oneformer 모델 구현
  + oneformer 기반 pre-labeling json 파일 출력 코딩 완료
+ RectLabel Modification
  + oneformer json output interaction 구현 완료 (coco dataset format)
  + RectLabel Tool 사용법 공부
  + RectLabel에서 "import coco json file"으로 Import Json 가능
  + json 파일 자동으로 전체 이미지 파일에 대해 매칭하는 부분 구현 완료
+ Labeling Guideline
  + 현재 가이드라인 작성 완료
  + 프로그램 동작하면서 error/노하우 정리 추가 에정
+ PanopticFCN input json/images 생성
  + PanopticFCN DeepLab 모델 코드 분석
  + input json/images 형태로 변환 코드 작성 (Python)
  + InstanceIds.png / color.png / labelIds.png 생성
  + InstanceIds.png ->  
    RectLabel에서 Export한 all_objects.png (indexed color mask images using class ID) + coco.json (annotations/counts 정보)
  + color.png 생성 완료
  + labelIds.png 생성 완료
+ 자동화 스크립트 생성
  + main.py 완료
  + instance_pixel_all_object_multi.py 수정 -> instance.py 완료
+ Unlabeled 매핑
  + 중복으로 labeling된 부분은 어떻게 처리? -> 둘 중 한 개의 객체로 자동 labeling됨
___

### 1. Pre-segmentation using OneFormer Model
  
+ (input) sample img -> (output) OneFormer_coco
  > run oneformer_convert_coco_json.ipynb
  + RectLabel import할 coco json 생성
  + OneFormer 모델 (Panoptic Segmentation 높은 정확도)

### 2. Panoptic FCN input img & json
  
+ (input) Screenshots -> (output) Color
  > run create_RGBA_multi.py
  + gtFine_color.png 생성
  + 투명도 포험, 파일 이름 변경

+ (input) All objects & RectLabel_coco json -> (output) InstanceIds
  > run instance_pixel_all_object_multi.py
  + gtFine_instanceIds.png 생성
  + 사람, 자동차 등 (인스턴스 구분 가능한) 객체들 카테고리 ID 입력

+ (input) All objects -> (output) LabelIds
  > run rename.py
  + gtFine_labelIds.png 생성
  + 파일 이름 변경
  
+ (input) Labelme json -> (output) Polygon json
  > run create_FCN_json.ipynb & run check_polygons_error.py
  + gtFine_polygons.json 생성

___

### Main 실행

+ python instanceIds.py <이미지 폴더 경로> <JSON 파일 경로>
+ python main.py <이미지 폴더 경로>



