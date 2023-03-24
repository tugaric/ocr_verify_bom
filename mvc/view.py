import io
import tkinter as tk
from PIL import ImageGrab, ImageTk

class view:
    def __init__(self):
        # Create the Tkinter window
        self.root = tk.Tk()
        self.root.title('Screenshot Viewer')
        self.root.minsize(400,300)

        # Create the label to display the image
        self.label = tk.Label(self.root)
        self.label.grid(column=0, row=0)

        self.btn_check = tk.Button(self.root, text= "Check bom", activebackground="blue", activeforeground="white")
        self.btn_check.grid(column=1, row=0)

    def run(self):
        # Start the main loop
        self.root.mainloop()

    def set_image(self, image):
        self.label.configure(image = image)
        self.label.image = image
