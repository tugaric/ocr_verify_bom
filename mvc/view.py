import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab, ImageTk, Image

class view:
    def __init__(self):
        # Create the Tkinter window---------------------------
        self.root = tk.Tk()
        self.root.title('Screenshot Viewer')
        self.root.minsize(400,300)
        # create the secondary window(s) & hide on program start
        self.screenshot_window = ScreenshotTaker("800x600")
        self.screenshot_window.hide_window()
    # load icons------------------------------------------
        # check_bom_button
        icon_check_bom = Image.open("icons\check_bom.png")
        self.tk_img_check_bom = ImageTk.PhotoImage(icon_check_bom)

    # screenshot_button
        icon_screenshot = Image.open("icons\icon_screenshot.png")
        icon_screenshot = icon_screenshot.resize((64, 64))
        self.tk_img_screenshot = ImageTk.PhotoImage(icon_screenshot)

        self.my_frame = tk.Frame(self.root)
        self.my_frame.grid(row=0, column=2)

    # Create the label to display the image
        self.lbl_active_image = tk.Label(self.root)
        self.lbl_active_image.grid(column=0, row=0, rowspan=2)

        self.btn_check =            ttk.Button(self.my_frame, image=self.tk_img_check_bom, text= "Check bom", style="TButton")
        self.btn_check.grid(column=1, row=0, sticky="NWE")

        self.btn_take_screenshot =  ttk.Button(self.my_frame, image=self.tk_img_screenshot, text= "Take screenshot", style="TButton")
        self.btn_take_screenshot.grid(column=1, row=1, sticky="NWE")

        options = []
        self.selected_value = tk.StringVar()
        self.cbo_valve_serie = ttk.Combobox(self.root, textvariable = self.selected_value, values= options)
        self.cbo_valve_serie.grid(column=1, row=0, sticky="W")

        self.screenshot_taker = None

    def run(self):
        # Start the main loop
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

    def save_screenshot(self, image:Image) -> None:
        self.screenshot_image =  image
    
    def get_screenshot(self) -> Image:
        return self.screenshot_image