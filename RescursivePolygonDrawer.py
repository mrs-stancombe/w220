# Write your code here :-)
import turtle

# creating turtle pen
t = turtle.Turtle

# make it pretty :-)
window = turtle.Screen()
window.bgcolor("lightgreen")

# define what the shape will look like
shape = turtle.Turtle()
shape.pensize(3)
turtle.title("Polygon Drawer")

print("Hello! Welcome to the polygon builder!")

# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))

# taking input for the length of the sides of the polygon
l = int(input("Enter the length of the sides of the polygon : "))

print("Okay! Time to draw your polygons :) ")

while n >= 3:
    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)
    n = n - 1
