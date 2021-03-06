import turtle as t
import random

timmy = t.Turtle()

color_list = [(232, 238, 246), (247, 238, 242), (239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

timmy.speed('fastest')
timmy.shape('arrow')
t.colormode(255)

def draw_dot(position):
  while position != 300:
    timmy.penup()
    timmy.goto(-230, position)
    timmy.pendown()
    for _ in range(10):
      timmy.dot(20, random.choice(color_list))
      timmy.penup()
      timmy.forward(50)
      timmy.pendown()

    position += 50
  timmy.ht()

draw_dot(-200)


screen = t.Screen()
screen.exitonclick()