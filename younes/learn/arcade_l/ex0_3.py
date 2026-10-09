import arcade

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__()
        self.center_window()
        self.background_color = arcade.color.BABY_BLUE_EYES
    def on_draw(self):
        self.clear()

def main():
    my_window = MyWindow()
    arcade.run()

main()