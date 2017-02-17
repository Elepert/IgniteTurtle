# this file has some examples of what Turtle graphics can do
# at the beginning of your Python file, make sure that you write:
import turtle

#writing with a hashtag in the front of it is a comment
#your computer won't process this writing when it runs code
new_turtle = turtle.Turtle()

def first_move(bob):
	bob.forward(100)
	bob.right(90)
	bob.forward(100)


first_move(new_turtle)

turtle.mainloop()
