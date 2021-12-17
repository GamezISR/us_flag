
import turtle

outside = turtle.Turtle()
stripe = turtle.Turtle()
union = turtle.Turtle()
star = turtle.Turtle()

def outside_flag():
  outside.speed(10)
  outside.pensize(1)
  outside.penup()
  outside.goto(-190,-100)
  outside.pendown()
  for i in range(2):
    outside.forward(380)
    outside.left(90)
    outside.forward(200)
    outside.left(90)

def union_box():
  union.speed(10)
  union_height = 200 * 0.5385
  union_width = 152
  union.penup()
  union.goto(-190,100)
  union.pendown()
  union.begin_fill()
  union.color(0,40,104)
  for i in range(2):
    union.forward(union_width)
    union.right(90)
    union.forward(union_height)
    union.right(90)
  union.end_fill()

def stripes():
  stripe_height = 200/13.0
  stripe_width = 380
  stripe.speed(100)
  stripe.penup()
  stripe.goto(-190,-100)
  for j in range(7):
    stripe.begin_fill()
    stripe.color(191,10,48)
    for i in range(2):
      stripe.forward(stripe_width)
      stripe.left(90)
      stripe.forward(stripe_height)
      stripe.left(90)
    stripe.end_fill()
    stripe.penup()
    stripe.left(90)
    stripe.forward(stripe_height*2)
    stripe.right(90)

def stars():
  star_size = 152 * .0616
  for i in range(5):
    star.color("white")
    star.forward(star_size)
    star.right(144)

def star_rows():
  h_distance = 200 * .063
  v_distance = 200 * .054 
  star.speed(100)
  
  star.penup()
  star.goto(-190 + h_distance/2,100 - v_distance/1.5)
  for j in range(5):
    for i in range(5):
      star.pendown()
      stars()
      star.penup()
      star.forward(h_distance * 2)
      star.pendown()
    stars()
    star.penup()
    star.backward(h_distance * 10)
    star.right(90)
    star.forward(v_distance * 2)
    star.left(90)
  star.penup()
  star.forward(v_distance*1.25)
  star.left(90)
  star.forward(v_distance*3)
  star.right(90)
  for i in range(4):
    for i in range(5):
      star.pendown()
      stars()
      star.penup()
      star.forward(h_distance * 2)
      star.pendown()
    star.penup()
    star.backward(h_distance * 10)
    star.left(90)
    star.forward(v_distance * 2)
    star.right(90)





outside_flag()
stripes()
union_box()
star_rows()


