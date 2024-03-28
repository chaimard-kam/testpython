from turtle import Shape, Turtle
from random import random



t = Turtle()

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")
# for i in range(10):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

s = Shape("compound")
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
s.addcomponent(poly1, "red", "blue")
poly2 = ((0,0),(10,-5),(-10,-5))
s.addcomponent(poly2, "blue", "red")

t.screen.mainloop()

