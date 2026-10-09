import arcade


class Tex:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_text(
            "younes",
            self.x,
            self.y,
            self.c,
            )


class TerO:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_triangle_outline(
            x1=self.x - self.w / 2, y1=self.y - self.h / 2,
            x2=self.x, y2=self.y + self.h / 2,
            x3=self.x + self.w / 2, y3=self.y - self.h / 2,
            color=self.c
        )

class TerF:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_triangle_filled(
            x1=self.x - self.w / 2, y1=self.y - self.h / 2,
            x2=self.x, y2=self.y + self.h / 2,
            x3=self.x + self.w / 2, y3=self.y - self.h / 2,
            color=self.c
        )

class CerO:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_circle_outline(
            self.x,
            self.y,
            self.w / 2,
            self.c
        )

class CerF:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_circle_filled(
            self.x,
            self.y,
            self.w / 2,
            self.c
        )

class RecO:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_rect_outline(
            arcade.XYWH(self.x, self.y, self.w, self.h),
            self.c
        )

class RecF:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_rect_filled(
            arcade.XYWH(self.x, self.y, self.w, self.h),
            self.c
        )


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__()
        self.center_window()
        self.background_color = arcade.color.DARK_BLUE_GRAY
        self.rec_f = RecF(self.width / 2 - 100, self.height / 2, 100, 100, arcade.color.YELLOW_ROSE)
        self.rec_o = RecO(self.width / 2 + 100, self.height / 2, 100, 100, arcade.color.YELLOW_ROSE)
        self.cer_f = CerF(self.width / 2 - 100, self.height / 2 - 110, 100, 100, arcade.color.YELLOW_ROSE)
        self.cer_o = CerO(self.width / 2 + 100, self.height / 2 - 110, 100, 100, arcade.color.YELLOW_ROSE)
        self.ter_o = TerO(self.width / 2 + 100, self.height / 2 + 110, 100, 100, arcade.color.YELLOW_ROSE)
        self.ter_f = TerF(self.width / 2 - 100, self.height / 2 + 110, 100, 100, arcade.color.YELLOW_ROSE)

    def on_draw(self):
        self.clear()
        self.rec_f.draw()
        self.rec_o.draw()
        self.cer_f.draw()
        self.cer_o.draw()
        self.ter_o.draw()
        self.ter_f.draw()

def main():
    game = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()