# #Exercise 1
# result = float(input("Please enter your exam result: "))
# def calculate_grade(r):
#     if r < 60:
#         return "F"
#     elif r < 70:
#         return "D"
#     elif r < 80:
#         return "C"
#     elif r < 90:
#         return "B"
#     else:
#         return "A"
# print("your grade is ", calculate_grade(result))

# #Exercise 2-3
# import turtle
# tur = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# def drawBar(tur, height, gap):
#     tur.penup()
#     tur.left(90)
#     if height > 0:
#         indication = 1
#     else:
#         indication = -1
#     tur.forward(height + gap*indication)
#     tur.write(" " + str(height))
#     tur.backward(height + gap*indication)
#     tur.right(90)
#     tur.pendown()
#
#     tur.begin_fill()
#     tur.left(90)
#     tur.forward(height)
#     tur.right(90)
#     tur.forward(40)
#     tur.right(90)
#     tur.forward(height)
#     tur.left(90)
#     tur.end_fill()
# def BarChart():
#     maxheight = max(data)
#     if min(data) < 0:
#         minheight = min(data)
#     else:
#         minheight = 0
#     num_bars = len(data)
#     border = 10
#
#     gap = (maxheight - border) / 25
#
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#     screen.setworldcoordinates(-border, -border + minheight, right, top)
#     tur.color("blue")
#     tur.pensize(3)
#     for height in data:
#         if height > 200:
#             tur.fillcolor("red")
#         elif height >= 100:
#             tur.fillcolor("yellow")
#         else:
#             tur.fillcolor("green")
#         drawBar(tur, height, gap)
# data = [-48, 117, 200, -240, 160, 260, -220]
# tur.speed(100)
# BarChart()
# screen.exitonclick()

#Exercise 4
x = float(input("The weight of the triangle: "))
y = float(input("The height of the rectangle: "))
def findHypot():
    answer = float(x ** 2 + y ** 2) ** 0.5
    return(answer)
print("hipotenus is ",findHypot())
