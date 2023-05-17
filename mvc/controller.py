import cv2
from PIL import ImageGrab, ImageTk, Image

# custom modules
from mvc.model import My_model, from_json_file
from mvc.view import view, ScreenshotTaker
from mvc.functions import show_image, image_to_text_position, filter_text_points, draw_rects_on_img

class controller:
    def __init__(self):
        self.model = My_model()
        self.view = view()

    def setup(self):
        # retrieve all the valve_boms_by_serie
        valves = from_json_file("valves.json")
        keys = list(valves.keys())
        
        # set initial image
        root_image = Image.open(r"images/init.png")
        root_tk_image = ImageTk.PhotoImage(root_image)
        self.view.set_image(root_tk_image)

        # set the series to the combobox as options
        self.view.set_combobox_values(keys)

        """" bind functions to the interactive widgets """
        self.view.btn_check.bind('<Button-1>', self.btn_check_bom_pressed)
        self.view.btn_open_screenshot_window.bind('<Button-1>', self.btn_open_screenshot_window_pressed)
        self.view.screenshot_window.btn_take_a_screenshot.bind('<Button-1>', self.secondary_window_screenshot_btn_pressed)
        self.view.run()

    """ Take screenshot once secondary window is open """
    def secondary_window_screenshot_btn_pressed(self, event):
        """ Button in screenshotTaker widget got pressed """
        """ Hide the secondary window so we can take the screenshot @ the wished position """
        toplevel_window = self.view.screenshot_window
        toplevel_window.hide_window()
        x, y = toplevel_window.winfo_x(), toplevel_window.winfo_y()
        w, h = toplevel_window.winfo_width(), toplevel_window.winfo_height()
        
        # Take a screenshot of the desktop
        img = ImageGrab.grab(bbox=(x, y, x + w, y + h))

        # save to the screenshot object
        toplevel_window.set_screenshot_image(img)
        screenshot = toplevel_window.get_screenshot()
        screenshot.save("images/screenshot.png")
        tk_image = ImageTk.PhotoImage(screenshot)
        self.view.set_image(tk_image)

    """ Open screenshot secondary window """
    def btn_open_screenshot_window_pressed(self, event):
        """ create the screenshot_taker instance """
        if self.view.screenshot_window not in self.view.root.winfo_children():
            self.view.screenshot_window = ScreenshotTaker("800x600")
        """ retrieve image """
        self.view.screenshot_window.show_window()

    """ user asking for image analysis / bom verification """
    def btn_check_bom_pressed(self, event):
        # get the serie selected in the combobox
        selected_serie = self.view.cbo_valve_serie.get()
        # retrieve the serie's corresponding bom
        boms_of_valve_serie = from_json_file("valves.json")
        serie_bom = boms_of_valve_serie[selected_serie]
        articles = list(serie_bom.keys())

        # get the image to be analyzed
        img = cv2.imread("images/screenshot.png")

        # pass the serie and the image to a function or class that evaluates the image
        # get a list with every text and textposition
        list_of_text_points = image_to_text_position(img)

        # compare the results with the article numbers we are searching
        filtered_text_positions = filter_text_points(serie_bom, list_of_text_points)

        # draw rectangles on every datapoint
        img_with_rect = draw_rects_on_img(img, filtered_text_positions)

        # show the result
        show_image(img_with_rect)