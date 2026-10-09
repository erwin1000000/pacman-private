import arcade

class ClickableButton:
    def __init__(self, x, y, w, h, t, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw(self):
        arcade.draw_rect_filled(
            arcade.XYWH(
                self.x,
                self.y,
                self.w,
                self.h
            ),
            self.c
        )
        arcade.Text(
            self.t,
            self.x,
            self.y,
            arcade.color.YELLOW,
            16,
            None,
            "left",
            "PAC-FONT.TTF",
            
        )
