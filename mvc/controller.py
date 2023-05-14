from mvc.model import My_model, from_json_file
from mvc.view import view
from mvc.functions import show_image, grab_screen_shot, get_keys_as_list, image_to_text_position, filter_text_points, draw_rects_on_img
from PIL import ImageGrab, ImageTk, Image
from mvc.ScreenshotTaker import ScreenshotTaker
import cv2

class controller:
    def __init__(self):
        self.model = My_model()
        self.view = view()

    def setup(self):
        # retrieve all the valve_boms_by_serie
        valves = from_json_file("valves.json")
        keys = get_keys_as_list(valves)
        
        # set initial image
        image = Image.open(r"images/init.png")
        tk_img = ImageTk.PhotoImage(image)
        self.view.set_image(tk_img)

        # set the series to the combobox as options
        self.view.set_combobox_values(keys)

        # bind functions to the interactive widgets
        self.view.root.bind('<Control-v>', self.display_screenshot)
        self.view.btn_check.bind('<Button-1>', self.btn_check_bom_pressed)
        self.view.btn_take_screenshot.bind('<Button-1>', self.btn_take_screenshot_pressed)
        self.view.run()

    """User wants screenshot"""
    def btn_take_screenshot_pressed(self, event):
        # create ScreenshotTaker 
        screenshot_taker = ScreenshotTaker("800x600")
        screenshot_taker.run()
        # retrieve image
        screenshot_taker = screenshot_taker.get_screenshot()
        # Save to screenshot.png for further treatement
        screenshot_taker.save("images/screenshot.png")

    def display_screenshot(self, event=None):
        # get screenshot
        image = grab_screen_shot()
        image.save(r"images/screenshot.png", format="PNG")
        # convert to a tkinter image
        photo_image = ImageTk.PhotoImage(image)
        # Update the self.view.label with the new image
        self.view.set_image(photo_image)
        self.view.root.update()
    # user asking for image analysis / bom verification
    def btn_check_bom_pressed(self, event):
        # get the serie selected in the combobox
        selected_serie = self.view.cbo_valve_serie.get()
        # retrieve the serie's corresponding bom
        boms_of_valve_serie = from_json_file("valves.json")
        articles = list(boms_of_valve_serie[selected_serie].keys())
        # get the image to be analyzed
        img = cv2.imread("images/screenshot.png")
        # pass the serie and the image to a function or class that evaluates the image
        # get a list with every text and textposition
        list_of_text_points = image_to_text_position(img)
        # compare the results with the article numbers we are searching
        filtered_text_positions = filter_text_points(articles, list_of_text_points)
        # draw rectangles on every datapoint
        img_with_rect = draw_rects_on_img(img, filtered_text_positions)
        # show the result
        show_image(img_with_rect)