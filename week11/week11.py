# #Exercise 1
# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
# fizz_buzz(16)

# #Exercise 2
# def digit_sum(n):
#     sum = 0
#     if type(n) is not int:
#         x = input("Please enter an integer: ")
#         digit_sum(x)
#     for i in str(abs(n)):
#         sum += int(i)
#     return sum
# print(digit_sum(1312312))

# #Exercise 3
# def alternate_case(s):
#     char_n = 0
#     new_str = ''
#     for char in s:
#         if char_n % 2 == 0:
#             new_str = new_str + char.upper()
#         elif char_n % 3 == 0:
#             new_str = new_str + char.lower()
#         else:
#             new_str = new_str + char
#         char_n += 1
#     return new_str
# print(alternate_case("Hello Folks"))

# #Exercise 4
# import turtle
# kamil = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# kamil.up()
# kamil.pensize(3)
# kamil.goto(-150, -30)
# kamil.down()
#
# def draw_polygon(t, sides, length):
#     angle = 180 - ((sides - 2) * 180 / sides)
#     for i in range(sides):
#         t.forward(length)
#         t.left(angle)
# def draw():
#     colors = ["red", "yellow", "blue"]
#     for i in range(3,6):
#         kamil.pencolor(colors[i-3])
#         draw_polygon(kamil, i, 60)
#         kamil.up()
#         kamil.forward(120)
#         kamil.down()
# draw()
# screen.exitonclick()

# #Exercise 5
# import turtle
# kamil = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# kamil.up()
# kamil.goto(-165,-25)
# kamil.down()
# def filled_square(t, size, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
# def draw():
#     for i in range(5):
#         if i % 2 == 0:
#             filled_square(kamil, 50, "red")
#         else:
#             filled_square(kamil, 50, "blue")
#         kamil.up()
#         kamil.forward(70)
#         kamil.down()
# draw()

# #Exercise 6
# import turtle
# folks = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# folks.pensize(2)
# def draw_square(t, size):
#     for i in range(4):
#         t.fd(size)
#         t.right(90)
# def draw():
#     for i in range(12):
#         draw_square(folks, 80)
#         folks.right(30)
# draw()
# screen.exitonclick()

# #Exercise 7
# import turtle
# kamil = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# kamil.up()
# kamil.goto(-120,-120)
# kamil.down()
#
# def chess_table(t, l):
#     for a in range(6):
#         t.left(90)
#         t.forward(l)
#         t.left(90)
#         t.forward(l*6)
#         t.right(180)
#
#         for b in range(6):
#             if b % 2 == 0 and a % 2 == 0 or b % 2 == 1 and a % 2 == 1:
#                 statement = True
#             else:
#                 statement = False
#             if statement:
#                 t.fillcolor("black")
#                 t.begin_fill()
#             for c in range(4):
#                 t.forward(l)
#                 t.right(90)
#             if statement:
#                 t.end_fill()
#             t.forward(l)
# chess_table(kamil, 40)
# screen.exitonclick()










