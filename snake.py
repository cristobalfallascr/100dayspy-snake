from turtle import Turtle
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.x
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def create_snake(self):
        self.x = 0
        for i in range(0, 3, 1):
            self.add_segment(i)


    def add_segment(self, segment):
        t = Turtle(shape="square")
        t.penup()
        t.color('white')
        t.goto(self.x, 0)
        self.x -= 20
        self.snake_body.append(t)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):

        for segment in self.snake_body:
            segment.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)
    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)