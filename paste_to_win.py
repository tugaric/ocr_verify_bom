import io
import tkinter as tk
from PIL import ImageGrab, ImageTk

def display_image(event=None):
    try:
        # Get the screenshot from the clipboard
        image = ImageGrab.grabclipboard()

        # If the clipboard contains an image
        if image:
            # Convert the image to a Tkinter-compatible format
            image_data = io.BytesIO()
            image.save(image_data, format='PNG')
            image_data.seek(0)
            photo_image = ImageTk.PhotoImage(data=image_data.getvalue())

            # Update the label with the new image
            label.configure(image=photo_image)
            label.image = photo_image
    except Exception as e:
        print(e)

# Create the Tkinter window
root = tk.Tk()
root.title('Screenshot Viewer')

# Create the label to display the image
label = tk.Label(root)
label.pack()

# Bind the "ctrl+v" keyboard shortcut to the display_image function
root.bind('<Control-v>', display_image)

# Start the main loop
root.mainloop()
