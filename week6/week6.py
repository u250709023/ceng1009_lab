# import turtle
# # -- setup --
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# # -- functions --
# def drawPoly(turtle, sides, size):
#     degree = (sides - 2)*180/ sides
#     for i in range(sides):
#         turtle.forward(size)
#         turtle.left(180-degree)
# def drawSpiral(turtle, angle):
#     size = 1
#     for i in range(100):
#         turtle.forward(size)
#         turtle.right(angle)
#         size += 2
# def drawEquitriangle(turtle, size):
#     drawPoly(turtle, 3, size)
# def drawStar(turtle, size):
#     for i in range(5):
#         turtle.forward(size)
#         turtle.right(144)
# def drawSprite(turtle, legs, lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         turtle.forward(lenght)
#         turtle.backward(lenght)
#         turtle.left(angle)
#

# -- exercises --
# # Exercise 1
# tess.color("pink")
# sides = int(input("Enter sides: "))
# size = int(input("Enter size: "))
# drawPoly(tess, sides, size)
# screen.exitonclick()

# #Exercise 2
# tess.pencolor("blue")
# for i in range(20):
#     drawPoly(tess, 4, 50)
#     tess.left(18)
# screen.exitonclick()

# # Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess, 89)
# screen.exitonclick()

# # Exercise 4
# drawEquitriangle(tess, 100)

# #Exercise 5
# tess.color("hotpink")
# for i in range(5):
#     drawStar(tess, 50)
#     tess.penup()
#     tess.forward(300)
#     tess.right(144)
#     tess.pendown()

# # Exercise 6
# drawSprite(tess, 15, 120)
# screen.exitonclick()