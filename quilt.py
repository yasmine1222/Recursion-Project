"""
Lab 7, Task 3

Using the turtle module, draws a Williams purple and gold quilt pattern.
"""
from turtle import *
from sys import argv

# Colors: Williams Purple and Gold.
PURPLE = '#500082'
GOLD = '#FFBE0A'

def draw_square(size, color):
    """Draws a single square of side length size (int) and given color (string)
    assuming turtle is initially at one of its endpoints. DO NOT MODIFY."""
    down()
    pen(fillcolor = color)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()
    up()

def initialize_turtle(size):
    """Setups up the window given size (int) and initializes the turtle to be at
    the bottom left corner of the pattern facing east (the default direction).
    DO NOT MODIFY."""

    # Create a turtle window
    padding = 50
    setup(width = size + padding, height = size + padding)
    reset()

    # Configure our turtles line width and speed
    pensize(1) 
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen and faces east.
    # We move it to the bottom left corner of the pattern.
    up()
    goto(-size/2, -size/2)


def draw_quilt(quilt_size, patch_size, patch_color, other_color):
    """Draws a colored quilt as described in the lab writeup.
    Assume that the turtle is positioned at the bottom left
    end point of quilt facing east before this function is called.
    """
    #initialize a base case
    if quilt_size<= patch_size:
        draw_square(quilt_size, patch_color)
        return 1
    #recursive call 
    else:
        #we draw the outer square
        draw_square(quilt_size, patch_color)
        #draw the bottom left square
        draw_square(quilt_size/2, patch_color)
        fd(quilt_size/2)
        #draw the bottom let quilt with our recursive function
        total1 =draw_quilt(quilt_size/2,patch_size,other_color,patch_color)
        lt(90)
        fd(quilt_size/2)
        rt(90)
        #draw the top right square
        draw_square(quilt_size/2, patch_color)
        bk(quilt_size/2)
        #draw the top left quilt with the recursive function
        total2= draw_quilt(quilt_size/2,patch_size,other_color,patch_color)
        #maintain invariance
        rt(90)
        fd(quilt_size/2)
        lt(90)
        return total1+total2
        

    
      

# When run as a script, take a picture size and the gap between
# concentric squares as command-line arguments.
if __name__=='__main__':
    """Testing code. DO NOT MODIFY."""
    if len(argv) != 3:
        print("Provide a quilt size and patch size when running, eg:\n")
        print("  python3 quilt.py 512 128\n")
    else:
        quilt_size = int(argv[1])
        patch_size = int(argv[2])

        initialize_turtle(quilt_size)
        num_squares = draw_quilt(quilt_size, patch_size, PURPLE, GOLD)
        getscreen().getcanvas().postscript(file="draw_quilt-{}-{}.ps".format(quilt_size, patch_size))
        print('draw_quilt({}, {}) -> {}'.format(quilt_size, patch_size, num_squares))

        # Comment out the line below if you want
        # the turtle screen to close automatically.
        exitonclick()
