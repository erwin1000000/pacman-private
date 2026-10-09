import arcade


class CenterRectangle:
  """Encapsulates the rectangle's properties and drawing logic."""

  def __init__(self, center_x: float, center_y: float, width: float, height: float, color):
    self.center_x = center_x
    self.center_y = center_y
    self.width = width
    self.height = height
    self.color = color

  def draw(self):
    # Convert center coordinates to bottom-left corner for Arcade's XYWH struct
    x = self.center_x - (self.width / 2)
    y = self.center_y - (self.height / 2)
    arcade.draw_rect_filled(arcade.XYWH(x, y, self.width, self.height), self.color)


class GameWindow(arcade.Window):
  """The central application window class."""

  def __init__(self, width: int, height: int, title: str):
    super().__init__(width, height, title)
    self.center_window()
    self.background_color = arcade.color.BABY_BLUE_EYES

    # Instantiate the rectangle using window dimensions once during setup
    self.myrect = CenterRectangle(
        center_x=self.width / 2,
        center_y=self.height / 2,
        width=200,
        height=100,
        color=arcade.color.RED,
    )

  def on_draw(self):
    self.clear()
    self.myrect.draw()


def main():
  # Define explicit screen boundaries
  window = GameWindow(800, 600, "Centered Rectangle Best Practice")
  arcade.run()


if __name__ == "__main__":
  main()