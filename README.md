# KETI Project1 (3/9~)
# Image-Segmentation, Auto Labeling
for Autonomous Driving and Real-time Object Detection

## OneFormer: One Transformer to Rule Universal Image Segmentation
### Panoptic Segmentation on Cityscapes
![keti1](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/28494afb-8720-495f-82b9-f6c5c01896d8)
![keti2](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/21ac4c95-80cf-416a-9262-9fd41385f48d)
![keti3](https://github.com/chaewonS/Image-Segmentation-Auto-Labeling/assets/81732426/c732ec8a-9580-4eb9-a106-b82686bb6cf0)

#### Use RectLabel(macOS) Segmentation Tool

![image](https://user-images.githubusercontent.com/81732426/228161115-16d28e8b-4570-4a09-bbea-b114960ad627.png)
#### Oneformer panoptic task ouput image

___

**구현 완료**
+ Pre-segmentation using SOTA
  + detectron2, oneformer 모델 구현
  + oneformer 기반 pre-labeling json 파일 출력 코딩 완료
+ RectLabel Modification
  + oneformer json output interaction 구현 완료
  + RectLabel Tool 사용법 공부
  + import coco json file
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

___

### <Pre-segmentation using OneFormer Model>

+ (input) sample img -> (output) OneFormer_coco
  > run oneformer_convert_coco_json.ipynb
  + RectLabel import할 coco json 생성
  + OneFormer 모델 (Panoptic Segmentation 높은 정확도)

### <Panoptic FCN input img & json>
  
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
  > run create_FCN_json.ipynb
  > run check_polygons_error.py
  + gtFine_polygons.json 생성




