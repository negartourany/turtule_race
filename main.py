from turtle import Screen, Turtle
import random
game = "off"
winner = ""
# turtles
turtle_1 = Turtle(shape="turtle")
turtle_2 = Turtle(shape="turtle")
turtle_3 = Turtle(shape="turtle")
turtle_4 = Turtle(shape="turtle")
turtle_5 = Turtle(shape="turtle")
turtle_6 = Turtle(shape="turtle")
turtle_1.penup()
turtle_2.penup()
turtle_3.penup()
turtle_4.penup()
turtle_5.penup()
turtle_6.penup()
# color
color = ["red", "orange", "blue", "yellow", "purple", "green"]
turtle_list = [turtle_1,turtle_2,turtle_3,turtle_4,turtle_5,turtle_6]

# screen
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Type a color: ")
# turtle color
turtle_1.color(color[0])
turtle_2.color(color[1])
turtle_3.color(color[2])
turtle_4.color(color[3])
turtle_5.color(color[4])
turtle_6.color(color[5])



# position of turtles

turtle_1.goto(x=-230,y=120)
turtle_2.goto(x=-230,y=70)
turtle_3.goto(x=-230,y=20)
turtle_4.goto(x=-230,y=-30)
turtle_5.goto(x=-230,y=-80)
turtle_6.goto(x=-230,y=-130)

if user_bet:
    game = "on"
while game =="on":
    for i in turtle_list:
        random_move = random.randint(0,10)
        i.forward(random_move)
        if i.xcor()>230:
            winner = i.pencolor()
            game = "off"
            break
if user_bet == winner:
    print("YOu have WOOn")
else:
    print(f"Sorry the winner was {winner}")
screen.exitonclick()