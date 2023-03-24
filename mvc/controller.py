from mvc.model import My_model, from_json_file
from mvc.view import view
from mvc.functions import grab_screen_shot, check_bom
from PIL import ImageGrab, ImageTk, Image

class controller:
    def __init__(self):
        self.model = My_model()
        self.view = view()

    def setup(self):
        self.view.root.bind('<Control-v>', self.display_image)
        self.view.btn_check.bind('<Button-1>', self.check_bom)
        self.view.run()

    def display_image(self, event=None):
        # get screenshot
        image = grab_screen_shot()
        image.save("screenshot.png", format="PNG")
        # convert to a tkinter image
        photo_image = ImageTk.PhotoImage(image)
        # Update the self.view.label with the new image
        self.view.set_image(photo_image)
        self.view.root.update()

    def check_bom(self, event=None):
    # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1

    # get the valve data
        valves = from_json_file("valves.json")
        components = valves[0]["C040"]
        path = "screenshot.png"
        result = check_bom(components, path)
        result = Image.fromarray(result)
        result.save("result.png")

if __name__ == "__main__":
    app = controller()
    app.setup()