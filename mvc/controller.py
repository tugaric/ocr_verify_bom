import io
import cv2
import numpy as np
from pytesseract import Output, pytesseract
from model import My_model, from_json_file
from view import view
from PIL import ImageGrab, ImageTk, Image

class controller:
    def __init__(self):
        self.model = My_model()
        self.view = view()

    def setup(self):
        self.view.root.bind('<Control-v>', self.display_image)
        self.view.btn_check.bind('<Button-1>', self.check_bom)
        self.view.run()

    def display_image(self, event=None):
        try:
            # Get the screenshot from the clipboard
            image = ImageGrab.grabclipboard()
            # If the clipboard contains an image
            if image:
                # Convert the image to a Tkinter-compatible format
                image_data = io.BytesIO()
                image.save("new_image.png", format= "PNG")
                image.save(image_data, format='PNG')
                image_data.seek(0)
                photo_image = ImageTk.PhotoImage(data=image_data.getvalue())
                # Update the self.view.label with the new image
                self.view.label.configure(image=photo_image)
                self.view.label.image = photo_image
        except Exception as e:
            print(e)

    def check_bom(self, event=None):
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1

        # get the valve data
        valves = from_json_file("valves.json")
        components = valves[0]["C040"]

        # Load the image
        img = cv2.imread('image.jpg')

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

if __name__ == "__main__":
    app = controller()
    app.setup()