import win32clipboard
from PIL import ImageGrab

# Get the image data from the clipboard
win32clipboard.OpenClipboard()
image_data = win32clipboard.GetClipboardData(win32clipboard.CF_BITMAP)
win32clipboard.CloseClipboard()

# Convert the image data to a PIL Image object
screenshot = ImageGrab.grabclipboard()

# Display the screenshot using the PIL Image show method
screenshot.show()