import turtle
import sys


window_size = 750
Windowz = turtle.Screen()
Windowz.setup(window_size, window_size)
Windowz.bgcolor('black')
Windowz.tracer(0)
Star = turtle.Turtle()
Star.color('white')


# will read from the Stars.text
Starinfo = open('Stars.txt', 'r')
# will write new data to the newStars.txt
newStars = open('newStars.txt', 'w')


def read_coords(Starinfo):
    henry_xy = {}  # gets the x and y coords
    henry_magnitude = {}  # gets the size
    name_and_henry = {}  # gets the constellation if it's there
    for line in Starinfo:
        line = line.strip()
        line = line.split(' ')
        henry_xy[line[3]] = (float(line[0]), float(line[1]))
        henry_magnitude[line[3]] = float(line[4])
        # these lines will check if there is anything at the 6th index
        # and adds them to that line's list
        try:
            if line[6] != '':
                names = " ".join(line[6:])
                names = names.split(';')
                for name in names:
                    name_and_henry[name] = line[3]
        except IndexError:
            pass
    plot_plain_Stars(window_size, henry_xy, henry_magnitude)


def plot_plain_Stars(picture_size, henry_xy, henry_magnitude):
    scaled_size = picture_size/2
    for item in henry_xy:
        # places the pen in the x, y quadrant
        if henry_xy[item][0] > 0 and henry_xy[item][1] > 0:
            Star.penup()
            Star.forward(henry_xy[item][0] * scaled_size)
            Star.left(90)
            Star.forward(henry_xy[item][1] * scaled_size)
            Star.begin_fill()
            size = Star_size(henry_magnitude[item])
            Star.pendown()
            for i in range(2):
                Star.right(90)
                Star.forward(size)
                Star.right(90)
                Star.forward(size)
            Star.end_fill()
            Star.penup()
            Star.goto(0, 0)
        # places the pen in the -x, y quadrant
        elif henry_xy[item][0] < 0 and henry_xy[item][1] > 0:
            Star.penup()
            Star.backward(henry_xy[item][0] * scaled_size)
            Star.left(90)
            Star.forward(henry_xy[item][1] * scaled_size)
            Star.begin_fill()
            size = Star_size(henry_magnitude[item])
            Star.pendown()
            for i in range(2):
                Star.right(90)
                Star.forward(size)
                Star.right(90)
                Star.forward(size)
            Star.end_fill()
            Star.penup()
            Star.goto(0, 0)
        # places the pen in the -x, -y quadrant
        elif henry_xy[item][0] < 0 and henry_xy[item][1] < 0:
            Star.penup()
            Star.backward(henry_xy[item][0] * scaled_size)
            Star.right(90)
            Star.forward(henry_xy[item][1] * scaled_size)
            Star.begin_fill()
            size = Star_size(henry_magnitude[item])
            Star.pendown()
            for i in range(2):
                Star.right(90)
                Star.forward(size)
                Star.right(90)
                Star.forward(size)
            Star.end_fill()
            Star.penup()
            Star.goto(0, 0)
        # places the pen in the x, -y quadrant
        elif henry_xy[item][0] > 0 and henry_xy[item][1] < 0:
            Star.penup()
            Star.forward(henry_xy[item][0] * scaled_size)
            Star.right(90)
            Star.forward(henry_xy[item][1] * scaled_size)
            Star.begin_fill()
            size = Star_size(henry_magnitude[item])
            Star.pendown()
            for i in range(2):
                Star.right(90)
                Star.forward(size)
                Star.right(90)
                Star.forward(size)
            Star.end_fill()
            Star.penup()
            Star.goto(0, 0)


def Star_size(henry_magnitude):
    Starsize = round(10.0/(henry_magnitude + 2))
    if Starsize > 8:
        Starsize = 8
    return Starsize

read_coords(Starinfo)

# somewhere we need to put in way to get the x and y coords multiply by
# scaled_size in order to keep them from being smashed together

