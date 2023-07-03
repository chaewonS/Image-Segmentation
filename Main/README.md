
![Image_segmentation_process](https://github.com/IoRTKETI/Pre-segmentation/assets/122510029/fc160f21-bf75-4cd7-8976-382405035071)


## Preparation
### CUDA 11.1 + Torch 1.9
``` pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html ```

### Install detectron2
``` python -m pip install 'git+https://github.com/facebookresearch/detectron2.git' ```  
``` git clone https://github.com/facebookresearch/detectron2.git ```  
``` python -m pip install -e detectron2 ```

### Install natten
``` pip3 install natten==0.14.2 -f https://shi-labs.com/natten/wheels/cu111/torch1.9/index.html ```

---
  
## Run
### (b) Pre-segmentation
- Pre-segmentation using SOTA
- oneFormer 기반으로 Json 파일 (pre-labeling 파일)을 출력하는 코딩 완료
- oneFomer Json을 RectLabel과 interaction 할 수 있도록 coco dataset format에 맞게 변환
- RectLabel에서 "Import COCO JSON file"으로 Import Json 가능
- run ``` oneformer_json.ipynb ```

### (c) PanopticFCN Train Json/Image
- ``` python instanceIds.py <이미지 폴더 경로> <COCO JSON 파일 경로> ```
- ``` python main.py <이미지 폴더 경로> ```
