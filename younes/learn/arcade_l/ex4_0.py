import arcade

class ClickableButton:
    def __init__(self, x, y, w, h, t, ct, cb):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        self.ct = ct
        self.cb = cb
        arcade.load_font("PAC-FONT.TTF")

    def draw(self):
        arcade.draw_rect_filled(
            arcade.XYWH(
                self.x,
                self.y,
                self.w,
                self.h
                ),
            self.cb
        )
        arcade.load_font("PAC-FONT.TTF")
        arcade.draw_text(
            "Pac-Man",
            self.x,
            self.y,
            self.ct,
            font_size=16,
            font_name="pacfont",
            anchor_x="center",
            anchor_y="center"
            )

    def is_clicked(self, x, y):
        l = self.x - (self.w / 2)
        r = self.x + (self.w / 2)
        t = self.y + (self.h / 2)
        b = self.y - (self.h / 2)
        return l <= x <= r and b <= y <= t

class RedView(arcade.View):
    def on_show_view(self):
        self.background_color = arcade.color.RED
        self.button = ClickableButton(
            self.window.width / 2,
            self.window.height / 2,
            200,
            100,
            "PacMan",
            arcade.color.YELLOW,
            arcade.color.BLACK
        )

    def on_draw(self):
        self.clear()
        self.button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.is_clicked(x, y):
            print("aaa")
            next_view = BlueView()
            self.window.show_view(next_view)

class BlueView(arcade.View):
    def on_show_view(self):
            self.background_color = arcade.color.BLUE
            self.button = ClickableButton(
                self.window.width / 2,
                self.window.height / 2,
                200,
                100,
                "PacMan",
                arcade.color.YELLOW,
                arcade.color.BLACK
            )
    
    def on_draw(self):
        self.clear()
        self.button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.is_clicked(x, y):
            print("aaa")
            next_view = GreenView()
            self.window.show_view(next_view)

class GreenView(arcade.View):
    def on_show_view(self):
        self.background_color = arcade.color.GREEN
        self.button = ClickableButton(
            self.window.width / 2,
            self.window.height / 2,
            200,
            100,
            "PacMan",
            arcade.color.YELLOW,
            arcade.color.BLACK
        )
    
    def on_draw(self):
        self.clear()
        self.button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.is_clicked(x, y):
            print("aaa")
            next_view = RedView()
            self.window.show_view(next_view)

def main():
    window = arcade.Window()

    start_view = RedView()
    window.show_view(start_view)

    arcade.run()

if __name__ == "__main__":
    main()
