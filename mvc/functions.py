from PIL import ImageGrab, ImageTk, Image
import cv2
import numpy as np
from pytesseract import Output, pytesseract

def get_keys_as_list(list_of_dictionaires):
    result = []
    for key in list_of_dictionaires.keys():
        result.append(key)
    return result

# return screenshot
def grab_screen_shot():
        try:
            # Get the screenshot from the clipboard
            image = ImageGrab.grabclipboard()
            # if image = NONE ( no value ) then if statement doesn't get executed
            if image:
                return image
            else:
                print("No screenshot available")
        except Exception as e:
            print(e)

def check_bom(components, image_path): #image_path = "image.jpg"
    # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1

    # Load the image
        img = cv2.imread(image_path)
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Threshold the image
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Remove noise
        thresh = cv2.medianBlur(thresh, 3)
        # Perform OCR on the image
        ocr_data = pytesseract.image_to_data(thresh, output_type=Output.DICT)
        for index, text in enumerate(ocr_data["text"]):
            #if text in components.keys():
            for key in components.keys():
                if key in text:
                    x1 = int(ocr_data["left"][index])
                    y1 = int(ocr_data["top"][index])
                    x2 = x1 + int(ocr_data["width"][index])
                    y2 = y1 + int(ocr_data["height"][index])
                    cv2.putText(img, components[key], (x1,y1-5), font, fontScale, color, thickness)
                    cv2.rectangle(img, (x1-2, y1-2), (x2+2, y2+2), (0, 255, 0), 1)
         # Display the result
        cv2.imshow('Result', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return img
       
