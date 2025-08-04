from ultralytics import YOLO


# the docs for hailo lib https://github.com/hailo-ai/hailo-apps-infra/blob/main/doc/README.md
# Load model

model = YOLO('yolo11n-seg.pt')  # Your segmentation model

# Run prediction
results = model("../test_img/", stream=True)


# For each detection
bi = []
for r in results:
    print(r)
    arr_boxes = []
    boxes = r.boxes  # Bounding boxes object
    if boxes != None:
        for b in boxes:
            x1,y1,x2,y2 = b.xyxyn.tolist()[0]
            tl,br = (x1,y1),(x2,y2)
            conf = float(b.conf)
            bi.append([(tl,br),conf])
            print("-"*100)
    print(bi)

    
        

