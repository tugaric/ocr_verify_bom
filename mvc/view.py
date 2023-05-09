import io
import tkinter as tk
from tkinter import ttk

from PIL import ImageGrab, ImageTk

class view:
    def __init__(self):
        # Create the Tkinter window
        self.root = tk.Tk()
        self.root.title('Screenshot Viewer')
        self.root.minsize(400,300)

        self.my_frame = tk.Frame(self.root)
        self.my_frame.grid(row=0, column=2)
        # Create the label to display the image
        self.label = tk.Label(self.root)
        self.label.grid(column=0, row=0, rowspan=2)

        self.btn_check = ttk.Button(self.my_frame, text= "Check bom", style="TButton")
        self.btn_check.grid(column=1, row=1)

        options = ["first", "second"]
        self.selected_value = tk.StringVar()
        self.cbo_valve_serie = ttk.Combobox(self.root, textvariable = self.selected_value, values= options)
        self.cbo_valve_serie.grid(column=1, row=0)

    def run(self):
        # Start the main loop
        self.root.mainloop()

    def set_combobox_values(self, options):
        # Remove any existing options from the dropdown
        self.cbo_valve_serie['values'] = options

        # Set the default value to the first option in the list
        self.cbo_valve_serie.current(0)

    def set_image(self, image_tk: ImageTk) -> None:
        self.label.configure(image = image_tk)
        self.label.image = image_tk
