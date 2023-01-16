import turtle 
import random 
  
  
t = turtle.Turtle() 
w = turtle.Screen() 
t.speed(0) 
w.bgcolor("black") 
t.color("white") 
w.title("Estrelas") 

def stars(): 
    for i in range(5): 
        t.fd(20) 
        t.right(144) 
  
  
for i in range(100): 
    
    
    x = random.randint(-640, 640) 
    y = random.randint(-330, 330) 
    stars() 
    t.up()     
    t.goto(x, y) 
    t.down() 
    
t.up() 
t.goto(0, 170) 
t.down() 
t.color("white") 
t.begin_fill() 
t.circle(5) 
t.end_fill() 
t.hideturtle() 
w.exitonclick() 