# this file has some examples of what Turtle graphics can do

# at the beginning of your Python file, make sure that you write:
import turtle
bob = turtle.Turtle()

def first_move(t):
    t.forward(100)
    t.right(90)
    t.forward(100)

first_move(bob)
turtle.mainloop()
