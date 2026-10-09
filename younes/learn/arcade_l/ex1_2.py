import arcade

class CenterRectangle:
    def __init__(self, center_x, center_y, width, height, color):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        # x = self.center_x - (self.width / 2)
        # y = self.center_y - (self.height / 2)
        arcade.draw_rect_filled(
            arcade.XYWH(self.center_x, self.center_y, self.width, self.height),
            self.color
        )

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__()
        self.center_window()
        self.background_color = arcade.color.BLACK_BEAN
        self.rec = CenterRectangle(
            self.width / 2,
            self.height / 2,
            100,
            100,
            arcade.color.GRAY
        )
    def on_draw(self):
        self.clear()
        self.rec.draw()

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()