#Given 2 points which form the lower left and top right coner of a rectangle
#write a function which outputs whether or not a 3rd point falls within
#a rectangle created by these 2 points



def insideRectangle(x1,y1,x2,y2,ax,ay):
    if ax<x2 and ax>x1:
      if ay < y2 and ay < y1:
        return True
    return False

print(insideRectangle(0,2,2,2,1,1))

def factorial(x):
    if x==1:
        return x
    return x * factorial(x-1)

def exp(base,power):
    if power == 1:
        return base
    else:
        return base * exp(base,power-1)

print(factorial(5))
print(exp(2,8))



