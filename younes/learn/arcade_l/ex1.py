import arcade



class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(resizable=True)
        self.center_window()
        self.background_color = arcade.color.DARK_SLATE_GRAY

    def on_draw(self):
        self.clear()
        
        # Arcade 3.x syntax taking an XYWH rectangle object
        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.width / 2, self.height / 2, 100, 100),
            arcade.color.AERO_BLUE
        )

def main():
    window = MyWindow()
    arcade.run()

if __name__ == "__main__":
    main()