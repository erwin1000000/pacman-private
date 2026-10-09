import arcade

# Constants for window dimensions and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Empty Arcade Window"

class MyWindow(arcade.Window):
    def __init__(self):
        # Call the parent class (arcade.Window) constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the background color
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

    def on_draw(self):
        # Clear the screen to the background color before drawing
        self.clear()

def main():
    # Instantiate the window
    window = MyWindow()
    
    # Keep the window open until the user closes it
    arcade.run()

if __name__ == "__main__":
    main()