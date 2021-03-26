import turtle


class Name:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(5)
        self.t.color('red')

    def start(self):
        while True:
            self.set_position()
            self.goto()
            self.write_p()
            self.write_e()
            self.write_d()
            self.write_r()
            self.write_o()

    def set_position(self, pos=0):
        self.t.seth(pos)

    def goto(self, x=-500, y=200):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def write_p(self):
        self.t.forward(100)
        self.t.rt(90)
        self.t.forward(100)
        self.t.rt(90)
        self.t.forward(100)
        self.t.rt(90)
        self.t.forward(100)
        self.t.rt(180)
        self.t.forward(200)

    def write_e(self):
        self.t.penup()
        self.goto(-350, 200)
        self.t.pendown()
        self.t.lt(90)
        self.t.forward(100)
        self.t.backward(100)
        self.t.right(90)
        self.t.forward(100)
        self.t.lt(90)
        self.t.forward(100)
        self.t.backward(100)
        self.t.right(90)
        self.t.forward(100)
        self.t.lt(90)
        self.t.forward(100)
        self.t.backward(100)

    def write_d(self):
        self.t.penup()
        self.goto(-200, 200)
        self.t.pendown()
        self.t.rt(30)
        self.t.forward(100)
        self.t.rt(60)
        self.t.forward(100)
        self.t.rt(60)
        self.t.forward(100)
        self.t.rt(120)
        self.t.forward(200)

    def write_r(self):
        self.t.rt(90)
        self.t.penup()
        self.goto(-50, 200)
        self.t.pendown()
        self.write_p()
        self.t.backward(100)
        self.t.lt(60)
        self.t.forward(115)
        self.t.rt(60)
        self.t.forward(40)

    def write_o(self):
        self.t.rt(90)
        self.t.penup()
        self.goto(200, 200)
        self.t.pendown()
        self.t.circle(100)


teste = Name()
teste.start()
