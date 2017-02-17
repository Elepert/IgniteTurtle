
import turtle

new_turtle = turtle.Turtle()

def square(bob):
	bob.forward(100)
	bob.right(90)
	bob.forward(100)
	bob.right(90)
	bob.forward(100)
	bob.right(90)
	bob.forward(100)


square(new_turtle)

turtle.mainloop()