# Lightweight Visual Detection Framework for Small Vehicles in UAV Aerial Highway Construction Scenes

This repository contains the official implementation of the paper submitted to **The Visual Computer**.

## Important Note
This code is directly related to the manuscript submitted to *The Visual Computer*.
If you use this code, please cite our paper.

---
# Citation
Once the paper is published, the full citation information will be provided here.For now, you may cite this repository as:
Zhou, J., Liu, J. (2026). Lightweight Visual Detection Framework for Small Vehicles in UAV Aerial Highway Construction Scenes. GitHub Repository. https://github.com/Azhou1999/LC-YOLO


1. Environment Installation
```bash
pip install ultralytics>=8.0.100
pip install torch torchvision opencv-python numpy

---
2. Configuration Instructions

The model configuration file is: LC-YOLO.yaml
This model integrates the C2f_LSKA_Attention module, which shows significant gains when used in the neck network.
The performance of this module may vary across tasks and positions. Users can adjust its position based on their own needs.
Please modify the file path parameters in the configuration according to your local file path.

3. Dataset Preparation
Organize your dataset in YOLO format:
datasets/
├── images/
│   ├── train/
│   ├── val/
└── labels/
    ├── train/
    └── val/

4. Training
yolo detect train model=LC-YOLO.yaml data=your_data.yaml epochs=400 batch=8 imgsz=640

6. Inference
yolo detect predict model=path/to/best.pt source=path/to/image

7. Code Availability
GitHub: https://github.com/Azhou1999/LC-YOLO

8. Detailed access information for each dataset is provided as follows.
UAV-HLCV: This dataset can be freely downloaded from Baidu Netdisk via the following permanent link: https://www.123865.com/s/hwQ8jv-Yb7Kd?pwd=1999 #. Visdrone: This dataset is accessible through the dedicated sharing link: https://github.com/VisDrone/VisDrone-Dataset. Construction PPE: Researchers can obtain this data set from the link: https://www.123865.com/s/hwQ8jv-eY7Kd, with access password: s5RA. The link and password are maintained to ensure long-term retrievability of the dataset. 



