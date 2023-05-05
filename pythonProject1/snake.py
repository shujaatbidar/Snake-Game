from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_new(i)

    def add_new(self, position):
        shape = Turtle("square")
        shape.color("white")
        shape.penup()
        shape.goto(position)
        self.segments.append(shape)

    def extend(self):
        self.add_new(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)

    def left(self):
        self.head.left(90)

    def right(self):
        self.head.right(90)


