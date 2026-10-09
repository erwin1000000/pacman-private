import arcade


class ClickableButton:
  """A custom button class that handles drawing and click detection."""

  def __init__(self, center_x: float, center_y: float, width: float, height: float, text: str, color):
    self.center_x = center_x
    self.center_y = center_y
    self.width = width
    self.height = height
    self.text = text
    self.color = color

  def draw(self):
    # Calculate bottom-left coordinates for Arcade's XYWH struct

    # Draw button background
    arcade.draw_rect_filled(arcade.XYWH(self.center_x, self.center_y, self.width, self.height), self.color)

    # Draw button label centered
    arcade.load_font("PAC-FONT.TTF")
    arcade.draw_text(
        self.text,
        self.center_x,
        self.center_y,  # Minor vertical adjustment to center text
        arcade.color.YELLOW,
        font_size=64,
        anchor_x="center",
        anchor_y="center",
        font_name="Pacfont"
    )

  def is_clicked(self, x: float, y: float) -> bool:
    """Check if given mouse coordinates fall inside the button boundaries."""
    left = self.center_x - (self.width / 2)
    right = self.center_x + (self.width / 2)
    bottom = self.center_y - (self.height / 2)
    top = self.center_y + (self.height / 2)

    return left <= x <= right and bottom <= y <= top


class GameWindow(arcade.Window):

  def __init__(self, width: int, height: int, title: str):
    super().__init__(width, height, title)
    self.center_window()

    # Define color sequence and initial index
    self.color_sequence = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN]
    self.color_index = 0
    self.background_color = self.color_sequence[self.color_index]

    # Initialize a centered button
    self.button = ClickableButton(
        center_x=self.width / 2,
        center_y=self.height / 2,
        width=600,
        height=300,
        text="PacMan",
        color=arcade.color.BLACK,
    )

  def on_draw(self):
    self.clear()
    self.button.draw()

  def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
    # Check if left mouse button was clicked
    if button == arcade.MOUSE_BUTTON_LEFT:
      # Check if the click coordinates hit the button
      if self.button.is_clicked(x, y):
        # Move to the next color, looping back to 0 using modulo arithmetic
        self.color_index = (self.color_index + 1) % len(self.color_sequence)
        self.background_color = self.color_sequence[self.color_index]


def main():
  window = GameWindow(800, 600, "Button Color Cycler")
  arcade.run()


if __name__ == "__main__":
  main()