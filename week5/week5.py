# import random
#
# for i in range(10):
#     number = random.random()
#     print(number)

# import random
#
# for i in range(10):
#     number = random.randrange(25,35)
#     print(number)

# import math
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# hypotenuse = math.hypot(length,width)
# print(hypotenuse)

# import math
# def areaOfCircle(r):
#     return math.pi * r**2
# radius = float(input("Enter the radius of the circle: "))
# print(areaOfCircle(radius))

# import turtle
# screen = turtle.Screen()
# obj = turtle.Turtle()
# size = 100
# def create_star(t, size=100):
#     for i in range(5):
#         t.forward(size)
#         t.right(144)
# create_star(obj, size)
# screen.exitonclick()

# import turtle
# obj = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# obj.pencolor("pink")
# obj.penup()
# obj.setpos(-60,0)
# obj.pensize(2)
# def drawSquare(obj):
#     for i in range(5):
#         obj.pendown()
#         for i in range(4):
#             obj.forward(20)
#             obj.left(90)
#         obj.penup()
#         obj.forward(40)
# drawSquare(obj)
# screen.exitonclick()

# import turtle
# obj = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# obj.pencolor("pink")
# obj.pensize(2)
# def drawSquares(obj):
#     sqr_size = 20
#     for i in range(5):
#         obj.pendown()
#         for i in range(4):
#             obj.forward(sqr_size)
#             obj.left(90)
#         obj.penup()
#         obj.right(135)
#         obj.forward(10 * 2**0.5)
#         obj.left(135)
#         sqr_size += 20
# drawSquares(obj)
# screen.exitonclick()





