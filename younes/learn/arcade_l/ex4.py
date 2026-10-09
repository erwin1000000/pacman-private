import arcade

class ClickableButton:
    """A reusable button class for any view."""
    def __init__(self, center_x: float, center_y: float, width: float, height: float, text: str):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.color = arcade.color.DARK_SLATE_GRAY

    def draw(self):
        arcade.draw_rect_filled(arcade.XYWH(self.center_x, self.center_y, self.width, self.height), self.color)
        
        arcade.draw_text(
            self.text,
            self.center_x,
            self.center_y - 8,
            arcade.color.WHITE,
            font_size=16,
            anchor_x="center",
        )

    def is_clicked(self, x: float, y: float) -> bool:
        left = self.center_x - (self.width / 2)
        right = self.center_x + (self.width / 2)
        bottom = self.center_y - (self.height / 2)
        top = self.center_y + (self.height / 2)
        return left <= x <= right and bottom <= y <= top


class RedView(arcade.View):
    def on_show_view(self):
        """Called when this view becomes active. Great for setting up UI."""
        self.background_color = arcade.color.RED
        self.button = ClickableButton(
            self.window.width / 2, self.window.height / 2, 200, 60, "Switch to Blue"
        )

    def on_draw(self):
        self.clear()
        self.button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.is_clicked(x, y):
            # Instantiate the next view and tell the window to show it
            next_view = BlueView()
            self.window.show_view(next_view)


class BlueView(arcade.View):
    def on_show_view(self):
        self.background_color = arcade.color.BLUE
        self.button = ClickableButton(
            self.window.width / 2, self.window.height / 2, 200, 60, "Switch to Green"
        )

    def on_draw(self):
        self.clear()
        self.button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.is_clicked(x, y):
            next_view = GreenView()
            self.window.show_view(next_view)


class GreenView(arcade.View):
    def on_show_view(self):
        self.background_color = arcade.color.GREEN
        self.button = ClickableButton(
            self.window.width / 2, self.window.height / 2, 200, 60, "Switch to Red"
        )

    def on_draw(self):
        self.clear()
        self.button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.is_clicked(x, y):
            next_view = RedView()
            self.window.show_view(next_view)


def main():
    # The Window is now just a blank container. It holds no logic of its own.
    window = arcade.Window(800, 600, "Multi-View Button Switcher")
    
    # Instantiate the first view and display it
    start_view = RedView()
    window.show_view(start_view)
    
    arcade.run()

if __name__ == "__main__":
    main()