from turtle import *


def square(side_len):
    """
    Function to draw a square in turtle
    """

    for i in range(4):
        fd(side_len)
        lt(90)

def polygon(side_len, num_sides):
    """
    Function to draw a polygon in turtle
    """

    for i in range(num_sides):
        fd(side_len)
        lt(360/num_sides)


def square_recursive(side_len, sides_left):
    """
    Function to draw a square recursively
    """

    if sides_left == 0:
        pass
    else:
        fd(side_len)
        lt(90)
        square_recursive(side_len, sides_left-1)

def spiral(side_len, sides_left, angle, shrink_factor):
    """
    Function to draw spirals
    """

    if sides_left == 0:
        pass
    else:
        fd(side_len)
        lt(angle)
        spiral(side_len*shrink_factor, sides_left-1, angle, shrink_factor)


def length_list(nums):
    """
    Function to compute length of list
    """

    if len(nums) == 0:
        return 0
    else:
        rest = nums[1:]
        return 1 + length_list(rest)

def concentric_circles(radius, gap, min_radius):
    """
    Function to draw concentric circles
    """

    if radius < min_radius:
        return 0

    else:
        down()
        circle(radius)
        up()
        lt(90)
        fd(gap)
        rt(90)
        num = concentric_circles(radius-gap, gap, min_radius)
        rt(90)
        fd(gap)
        lt(90)
        return 1 + num

def color_circle(radius, color):
    """
    Function to draw a circle filled with a given color
    """
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def concentric_color(radius, gap, min_radius, color1, color2):
    """
    Function to draw concentric circles with alternating colours
    """

    if radius < min_radius:
        return 0

    else:
        down()
        color_circle(radius, color1)
        up()
        lt(90)
        fd(gap)
        rt(90)
        num = concentric_color(radius-gap, gap, min_radius, color2, color1)
        rt(90)
        fd(gap)
        lt(90)
        return num + 1


def nested_circles(radius, min_radius, color1, color2):
    """
    Function to draw nested circles
    """

    if radius < min_radius:
        return 0
    else:
        down()
        # draw current circle
        color_circle(radius, color1)
        half_radius = radius/2

        # reposition and draw right subcircle
        up(); lt(90); fd(half_radius); rt(90); fd(half_radius)
        down()
        num_right = nested_circles(half_radius, min_radius, color2, color1)

        # reposition and draw left subcircle
        up(); bk(radius)
        down()
        num_left = nested_circles(half_radius, min_radius, color2, color1)

        # commands for function invariance
        up(); fd(half_radius); rt(90); fd(half_radius); lt(90)

        return 1 + num_left + num_right







if __name__ == "__main__":

    # uncomment different things here to test out different functions
    
    setup(800, 800)
    shape("turtle")
    speed(100)
    # square(200)
    # polygon(50, 36)
    # square_recursive(200, 4)
    # spiral(200, 100, 80, 0.95)
    # circle(50)
    # concentric_circles(150, 15, 10)
    # num_circles = concentric_color(150, 15, 10, "purple", "gold")
    # print("Num circles", num_circles)

    print("Num nested circles", nested_circles(200, 10, "purple", "gold"))


    done()