from ultralytics import YOLO

model = YOLO('D:/ultralytics11.27/runs/detect/train210/weights/best.pt')

results = model('D:/ultralytics11.27/ultralytics/cfg/datasets/fire-smoke-dataset/train/images/08.jpg', save=True)
