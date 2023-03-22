import io
import tkinter as tk
from PIL import ImageGrab, ImageTk

class view:
    def __init__(self):
        # Create the Tkinter window
        self.root = tk.Tk()
        self.root.title('Screenshot Viewer')
        self.root.geometry("400x300")

        # Create the label to display the image
        self.label = tk.Label(self.root)
        self.label.grid(column=0, row=0)

        self.btn_check = tk.Button(self.root, text= "Check bom", activebackground="blue", activeforeground="white")
        self.btn_check.grid(column=1, row=0)

        # Bind the "ctrl+v" keyboard shortcut to the display_image function
        # self.root.bind('<Control-v>', display_image)

    def run(self):
        # Start the main loop
        self.root.mainloop()