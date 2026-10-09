import arcade


L3ARD = 800
TOL = 600
TITRE = "window khawya"

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(L3ARD, TOL, TITRE)
        self.center_window()
        # arcade.set_background_color(arcade.color.AERO_BLUE)
        self.background_color = arcade.color.WENGE
    def on_draw(self):
        self.clear()

def main():
    window = MyWindow()
    arcade.run()

if __name__ == "__main__":
    main()