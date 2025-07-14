from ultralytics import YOLO

# Load model
model = YOLO('yolo11n-seg.pt')  # Your segmentation model

# Run prediction
results = model("calib/", stream=True)
# results = model("calib/.")  # or a loop over your images

# For each detection
for r in results:
    boxes = r.boxes  # Bounding boxes object
    if True:
        for b in boxes:
            print(b)
            print(type(boxes))
            print(r)
            print("-"*100)