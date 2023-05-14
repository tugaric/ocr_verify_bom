import PIL
import tkinter as tk
from tkinter import ttk
import pyautogui
import numpy as np
from PIL import ImageGrab, ImageTk, Image
import cv2

def debug_img(pil_image):
    img = np.array(pil_image)
    cv2.imshow('Image', img)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the window

class ScreenshotTaker:
    def __init__(self, window_size:str):
        self.root = tk.Tk()
        self.root.geometry(window_size)
        self.screenshot_image = None
        self.root.attributes("-alpha", 0.75)
        icon_screenshot = Image.open(r"icons/icon_screenshot.png")
        icon_screenshot = icon_screenshot.resize((64, 64))
        self.tk_image = ImageTk.PhotoImage(icon_screenshot)
        # ------------------------------------------------------------
        self.button = ttk.Button(self.root, text="Take Screenshot", command=self.take_screenshot)
        self.button.pack()
        
    def set_icons(self, tk_img):
        if tk_img is not None:
            self.button.configure(image=tk_img)
        else:
            print("doesn't exist")

    def run(self):
        self.root.mainloop()

    def get_screenshot(self) -> PIL.Image:
        return self.screenshot_image

    def save_screenshot(self, image:PIL.Image) -> None:
        self.screenshot_image =  image

    def take_screenshot(self):
        self.root.withdraw()
        # Get the position and size of the Tkinter window
        x, y = self.root.winfo_x(), self.root.winfo_y()
        w, h = self.root.winfo_width(), self.root.winfo_height()
        
        # Take a screenshot of the desktop
        img = ImageGrab.grab(bbox=(x, y, x + w, y + h))

        # save to the screenshot object
        self.save_screenshot(img)

        # destroy the window used to define screenshot location
        self.root.quit()

if __name__ == "__main__":
    my_screenshot = ScreenshotTaker("800x600")
    
    my_screenshot.set_icons(tk_image)
    my_screenshot.run()
    image = my_screenshot.get_screenshot()

    # convert to array to be able to visualize it with cv2.imshow
    screenshot_np = np.array(image)
    cv2.imshow("Screenshot", screenshot_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()