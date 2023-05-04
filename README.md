# KETI Project1 (3/9~)
# Image-Segmentation, Auto Labeling
for Autonomous Driving and Real-time Object Detection

## OneFormer: One Transformer to Rule Universal Image Segmentation
### Panoptic Segmentation on Cityscapes
![image](https://user-images.githubusercontent.com/81732426/228160940-6a141375-df12-404c-aecc-348076e2cd34.png)
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
