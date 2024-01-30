'''
Created on Nov 30, 2018
@author: aaronfeinberg
'''
import turtle #well call him 'b'
wn=turtle.Screen()
wn.title("Can we pretend that airplanes,in the night sky are like...")

b = turtle.Turtle() 
b.speed(0)

for i in range(40):
    
    from random import*
    x_Cor = randint(-300,300)
    y_Cor = randint(-300,300)
    b.penup()
    b.setpos(x_Cor, y_Cor)
    
    for i in range(5):
        b.pendown()
        b.forward(50+x_Cor/10)
        b.right(144)
        
    b.penup()
    b.hideturtle()
        
        
        
    
    
wn.exitonclick()

    
        







