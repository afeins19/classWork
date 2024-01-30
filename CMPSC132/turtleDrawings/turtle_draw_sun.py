
'''
Created on Nov 30, 2018

@author: aaronfeinberg
'''
import turtle

#calls a new screen object from the turtle module
wn = turtle.Screen()       
wn.title("la tortuga esta dibujando!")   
 
#instantiation of the turtle object
tess = turtle.Turtle()       
tess.pensize(1)
tess.speed(0)

#drawing algorithm 
for i in range(200):
    tess.setpos(0, 0)
    tess.pendown()
    tess.forward(50)
    tess.right(15)
    tess.forward(i)
    
#hides turtle when drawing is finished 
#and waits for user to exit
    
tess.hideturtle()
wn.title("listo!")
wn.exitonclick()




    


        
        
        