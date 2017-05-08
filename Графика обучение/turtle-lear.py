#!/usr/bin/python3.5
#-*- codig:UTF-8 -*-
import turtle
turtle.reset()
turtle.speed(0)
turtle.tracer(0)
turtle.width(2)
turtle.color('red')
#face
turtle.up()
turtle.goto(0, -150)
#face_draw
turtle.down()
turtle.begin_fill()
turtle.circle(180)
turtle.end_fill()
#nose
turtle.up()
turtle.goto(-5, 120)
#nose_draw
turtle.down()
turtle.color('maroon')
turtle.goto(-15, 0)
turtle.right(90)
turtle.circle(15, 180)
turtle.goto(5, 120)
turtle.up()
#

turtle.goto(-125, -40)
turtle.down()
turtle.right(150)
#turtle.speed(1)
turtle.circle(150, 120)
print(turtle.pos())
turtle.up()
turtle.speed(0)
#
turtle.goto(-125, -40)
turtle.down()
turtle.right(105)
#turtle.speed(1)
turtle.circle(180, 92)
print(turtle.pos())
turtle.up()
#
turtle.goto( -50, 120)
turtle.down()
turtle.color('#254687')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.up()
#
turtle.goto( 100, 120)
turtle.down()
turtle.color('#254687')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.up()


turtle.mainloop()
