import arcade

class Cherjem(arcade.Window):
    def __init__(self):
        super.__init__(800, 800, "selfmade")
        self.center_window()
        self.background_color = arcade.color.ALABAMA_CRIMSON

    def on_draw(self):
        return super().on_draw()
    