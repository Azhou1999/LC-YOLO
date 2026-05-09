from ultralytics import YOLO


def main():
    # Load a model
    model = YOLO('LC-YOLO.yaml')

    model.train(data='D:/ultralytics11.27/data.yaml', epochs=400, imgsz=640)


if __name__ == '__main__':  # 不加这句就会报错
    main()  # 不加这句就会报错
