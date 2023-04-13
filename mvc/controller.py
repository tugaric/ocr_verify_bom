from mvc.model import My_model, from_json_file
from mvc.view import view
from mvc.functions import grab_screen_shot, check_bom, get_keys_as_list
from PIL import ImageGrab, ImageTk, Image
import cv2

class controller:
    def __init__(self):
        self.model = My_model()
        self.view = view()

    def setup(self):
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
        self.view.btn_check.bind('<Button-1>', self.check_bom)
        self.view.run()

    def display_screenshot(self, event=None):
        # get screenshot
        image = grab_screen_shot()
        image.save(r"images/screenshot.png", format="PNG")
        # convert to a tkinter image
        photo_image = ImageTk.PhotoImage(image)
        # Update the self.view.label with the new image
        self.view.set_image(photo_image)
        self.view.root.update()

    def check_bom(self, event):
        # location where the analyzed data get stored
        img_save_location_path = r"images/result.png"
        # location that contains the image of the bom to verify
        bom_location_path = r"images\screenshot.png"
        
        # get the valve json data
        valves = from_json_file("valves.json")
        keys = get_keys_as_list(valves)
        components = valves[self.view.cbo_valve_serie.get()]
        
        result = check_bom(components, bom_location_path)
        result = Image.fromarray(result)
        result.save(img_save_location_path)