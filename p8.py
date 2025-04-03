"""
QN:Write a python function to draw a square using turtle graphics(JUNE 2023)
"""
import turtle
def draw_square(t,side_length):
	for _ in range(4):  
        	t.forward(side_length)          
		t.left(90)  
t = turtle.Turtle()     
draw_square(t,100)
t.hideturtle() 
turtle.done()
