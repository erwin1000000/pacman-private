import arcade

L3ARD = 800
TOLE = 600
TITRE = "waaaaaaaaaa"

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(L3ARD, TOLE, TITRE)
        self.center_window()
        self.background_color = arcade.color.DARK_SLATE_GRAY
    def on_draw(self):
        self.clear()
    
def main():
    window = MyWindow()
    arcade.run()

if __name__ == "__main__":
    main()