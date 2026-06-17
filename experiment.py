import turtle
import random

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
my_turtle = turtle.Turtle()

def click_handler(x, y):
  my_turtle.forward(100)
  my_turtle.forward(-100)

my_turtle.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
