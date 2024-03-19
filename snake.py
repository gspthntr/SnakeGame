from turtle import Screen, Turtle
MOVE_DISTANCE = 10


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for _ in range(0, 3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.teleport(x, y)
            x -= 20
            self.segments.append(t)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def check_heading(self):
        current_heading = self.segments[0].heading()
        return current_heading

    def up(self):
        if self.check_heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.check_heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.check_heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.check_heading() != 180:
            self.segments[0].setheading(0)

    def new_segment(self):
        t = Turtle(shape="square")
        self.segments.append(t)
        t.penup()
        t.color("white")

    def collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 8:
                return True

    def out_of_bounds(self):
        if self.segments[0].xcor() > 280 or self.segments[0].ycor() > 280 or self.segments[0].xcor() < -280 or self.segments[0].ycor() < -280:
            return True

    def snake_reset(self):
        for segment in self.segments:
            segment.goto(x=1000, y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
