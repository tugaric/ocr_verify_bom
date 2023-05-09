from mvc.functions import *
from mvc.custom_dataclass import TextPosition
import cv2

if __name__ == "__main__":
    img = cv2.imread("images/screenshot.png")
    # get a list with every text and textposition
    list_of_text_points = image_to_text_position(img)
    # compare the results with the article numbers we are searching
    """"""
    # draw rectangles on every datapoint
    img_with_rect = draw_rectangles_on_text_points(img, list_of_text_points)
    # show the image
    show_image(img_with_rect)
