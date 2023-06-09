# standard libraries
import cv2
import numpy as np
from typing import List, Dict
from PIL import ImageGrab, ImageTk, Image
from pytesseract import Output, pytesseract
from mvc.custom_dataclass import TextPosition

def filter_text_points(dict_of_words: Dict[str, str], list_of_text_and_position: List[TextPosition]) -> List[TextPosition]:
    word_positions = {text_and_position.text: text_and_position for text_and_position in list_of_text_and_position}
    func_result = []

    for key, word in dict_of_words.items():
        if key in word_positions:
            text_position = word_positions[key]
            text_position.text = word
            func_result.append(text_position)

    return func_result

def image_to_text_position(img):
    """"""
    res_list = []
    ocr_data = pytesseract.image_to_data(img, output_type=Output.DICT)
    for index, text in enumerate(ocr_data["text"]):
        if text != "":
            """"""
            text = text
            x1 = int(ocr_data["left"][index])
            y1 = int(ocr_data["top"][index])
            x2 = x1 + int(ocr_data["width"][index])
            y2 = y1 + int(ocr_data["height"][index])
            new_text_position_point = TextPosition(text, x1, y1, x2, y2)
            res_list.append(new_text_position_point)
    return res_list

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

def image_transform(image_path: str) -> np.ndarray:
    # Load the image
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Remove noise
    thresh = cv2.medianBlur(thresh, 3)
    # Perform OCR on the image
    return img, gray

def draw_rects_on_img(img: np.ndarray, text_positions: TextPosition) -> Image:
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    color = (255, 0, 0)
    thickness = 1
    for tp_point in text_positions:
    # aliases for textbox position variables
        x1 = tp_point.x1
        y1 = tp_point.y1
        x2 = tp_point.x2
        y2 = tp_point.y2
        text_y_offset = 5
        # Draw rectangles and text on the given positions
        cv2.putText(img, tp_point.text, (x1,y1-text_y_offset), font, fontScale, color, thickness)
        # 2 is the offset, so the rectangle doesn't get drawn over the words
        cv2.rectangle(img, (x1-2, y1-2), (x2+2, y2+2), (0, 255, 0), 1)
        # return the completed image
    return img

def show_image(img:np.ndarray):
    """"""
    cv2.imshow('Originial', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()