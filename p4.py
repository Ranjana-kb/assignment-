"""
QN:Write a Python program to draw a hexagon and to fill it with red colour. Explain
the turtle methods used in it.(MAY 2023)
ANS:

   Method	                   Description
turtle.Turtle()	  :Creates a turtle object to draw shapes.
fillcolor("red")  :Sets the fill color to red.
begin_fill()	  :Marks the beginning of a filled shape.
for _ in range(6) :A loop to draw six sides of the hexagon.
forward(100)	  :Moves the turtle forward by 100 units.
left(60)	  :Turns the turtle left by 60° (hexagon has 120° interior angles).
end_fill()	  :Fills the shape with the previously set color.
hideturtle()	  :Hides the turtle pointer after drawing is complete.
turtle.done()	  :Keeps the drawing window open.

"""
#PROGRAM
import turtle
t = turtle.Turtle()


t.fillcolor("red")  
t.begin_fill()   
for _ in range(6):
    t.forward(100)  
    t.left(60)     

t.end_fill() 

t.hideturtle()
turtle.done()
