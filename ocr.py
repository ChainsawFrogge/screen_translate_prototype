import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_text_boxes(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    boxes = []

    for i in range(len(data["text"])):
        text = data["text"][i].strip()
        conf = int(data["conf"][i])

        if conf > 60 and len(text) > 1:
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]

            boxes.append({
                "text": text,
                "box": (x, y, w, h)
            })

    return boxes