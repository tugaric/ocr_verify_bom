import tkinter as tk
from PIL import Image, ImageTk
import io
import clipboard

def display_image(event):
    print("Ctrl+v")
    clipboard_content = clipboard.paste()
    if not clipboard_content.startswith('data:image/png'):
        error_label.config(text='Error: clipboard content is not an image')
        return
    image_data = clipboard_content.split(',', 1)[1].encode()
    image = Image.open(io.BytesIO(image_data))
    photo_image = ImageTk.PhotoImage(image)
    label.configure(image=photo_image)
    label.image = photo_image
    error_label.config(text='')

root = tk.Tk()
root.title('Screenshot Viewer')

label = tk.Label(root, text="Insert image here")
label.pack()

error_label = tk.Label(root, text="error message", fg='red')
error_label.pack()

root.bind("<Control-v>", display_image)

root.mainloop()
