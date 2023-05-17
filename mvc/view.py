import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab, ImageTk, Image

def icon_path_to_tk_img(icon_path):
    icon_screenshot = Image.open(icon_path)
    icon_screenshot = icon_screenshot.resize((64, 64))
    return ImageTk.PhotoImage(icon_screenshot)

class view:
    def __init__(self):
    # Create the main "root" window---------------------------
        self.root = tk.Tk()
        self.root.title('Bom verification')
        self.root.minsize(400,300)

        # create the secondary window(s) & hide on program start
        self.screenshot_window = ScreenshotTaker("800x600")

        # initially hide the window on creation has to only be shown if the user presses button
        self.screenshot_window.hide_window()

        """ --------------------load icons---------------------- """
        # check_bom_button
        self.tk_img_check_bom = icon_path_to_tk_img(icon_path = "icons\check_bom.png")
        self.tk_img_screenshot = icon_path_to_tk_img(icon_path = "icons\icon_screenshot.png")

        self.my_frame = tk.Frame(self.root)
        self.my_frame.pack()

    # Create the label to display the image
        self.lbl_active_image = tk.Label(self.my_frame)
        self.lbl_active_image.grid(column=0, row=1, rowspan=2)

        self.btn_check = ttk.Button(self.my_frame, image=self.tk_img_check_bom, text= "Check bom", style="TButton")
        self.btn_check.grid(column=1, row=1, sticky="NWE")

        self.btn_open_screenshot_window = ttk.Button(self.my_frame, image=self.tk_img_screenshot, text= "Take screenshot", style="TButton")
        self.btn_open_screenshot_window.grid(column=1, row=2, sticky="NWE")

        options = []
        self.selected_value = tk.StringVar()
        self.cbo_valve_serie = ttk.Combobox(self.my_frame, textvariable = self.selected_value, values= options)
        self.cbo_valve_serie.grid(column=0, row=0, sticky="W")

    def run(self):
        # Start the main "root" window loop
        self.root.mainloop()

    def set_combobox_values(self, options):
        # Remove any existing options from the dropdown
        self.cbo_valve_serie['values'] = options

        # Set the default value to the first option in the list
        self.cbo_valve_serie.current(0)

    def set_image(self, image_tk: ImageTk) -> None:
        self.lbl_active_image.configure(image = image_tk)
        self.lbl_active_image.image = image_tk

class ScreenshotTaker(tk.Toplevel):
    def __init__(self, window_size:str):
        super().__init__()
        self.geometry(window_size)
        self.screenshot_image = None
        self.attributes("-alpha", 0.75)
        icon_screenshot = Image.open(r"icons/icon_screenshot.png")
        icon_screenshot = icon_screenshot.resize((64, 64))
        self.tk_image = ImageTk.PhotoImage(icon_screenshot)
        # ------------------------------------------------------------
        self.btn_take_a_screenshot = ttk.Button(self, text="Take Screenshot", image=self.tk_image)
        self.btn_take_a_screenshot.pack()

    def show_window(self):
        self.deiconify()

    def hide_window(self):
        self.withdraw()

    def set_screenshot_image(self, image:Image) -> None:
        self.screenshot_image =  image
    
    def get_screenshot(self) -> Image:
        return self.screenshot_image