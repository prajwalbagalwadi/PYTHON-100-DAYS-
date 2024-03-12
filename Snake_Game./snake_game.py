# JAI SHREE RAM
# from turtle import Turtle

#  importing libaries 
import turtle as  t
import time 
import random 


from food import Food
from scoreboard import Scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
segments=[]
food=Food() 
scoreboard = Scoreboard()

def  RAM():
    t.color("orange")
    t.write(f"JAI SHREE RAM ", align=ALIGNMENT, font=FONT)
    t.update()
    time.sleep(2)
    t.clear()


def forword():
    # segments[0].forward(20)
    if segments[0].heading() != 270:
        segments[0].setheading(90)
def backward():
    # segments[0].backward(20)
    if segments[0].heading() != 90:
        segments[0].setheading(270)
def left():
    # segments[0].left(10)
     if segments[0].heading() != 0:
        segments[0].setheading(180)
def right():
    # segments[0].right(-10)
     if segments[0].heading() != 180:
        segments[0].setheading(0)
def move():
    t.listen()
    t.onkeypress(forword,"Up")
    t.onkeypress(backward,"Down")
    t.onkeypress(left,"Left")
    t.onkeypress(right,"Right")

t.tracer(0)
# t.screensize(canvwidth=600, canvheight=600, bg="black")
t.screensize(canvwidth=600, canvheight=600, bg="black")
RAM()


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
def next_sanke():
    new_segment=t.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)
    segments[-1].position()
        
for pos in STARTING_POSITIONS:
    next_sanke()
    
def movement():
    for  seg in range(len(segments)-1,0,-1):
        new_X=segments[seg-1].xcor()
        new_y=segments[seg-1].ycor()
        segments[seg].goto(new_X,new_y)
        
    segments[0].forward(20)

    move()
    
      


          
game_on=True
while(game_on):
    t.update()
    time.sleep(0.1)
    movement()
    if segments[0].distance(food)<15:
        food.refresh()
        next_sanke()
        scoreboard.increase_score()
    if segments[0].xcor()>950 or segments[0].xcor()<-950 or  segments[0].ycor()>500 or segments[0].ycor()<-500:
        game_on=False
        scoreboard.game_over()
    for segment in segments:
        if segment == segments[0]:
            pass
        elif segment.distance(segments[0]) < 10:
            game_on = False
            scoreboard.game_over()

    
         
       
        
    
        
        
        
    
        

     
    
    


    


    





t.exitonclick()
