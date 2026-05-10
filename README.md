# Lightweight Visual Detection Framework for Small Vehicles in UAV Aerial Highway Construction Scenes

This repository contains the official implementation of the paper submitted to **The Visual Computer**.

## Important Note
This code is directly related to the manuscript submitted to *The Visual Computer*.
If you use this code, please cite our paper.

---
# Citation
Once the paper is published, the full citation information will be provided here.For now, you may cite this repository as:
Zhou, J., Liu, J. (2026). Lightweight Visual Detection Framework for Small Vehicles in UAV Aerial Highway Construction Scenes. GitHub Repository. https://github.com/[YOUR_GITHUB_USERNAME]/LC-YOLO


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
GitHub: https://github.com/[你的 GitHub 名字]/LC-YOLO
DOI: [你的 DOI]



