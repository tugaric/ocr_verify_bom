"""
import PIL
import tkinter as tk
from tkinter import ttk
import pyautogui
import numpy as np
from PIL import ImageGrab, ImageTk, Image
import cv2

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
    """