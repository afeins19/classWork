import random
import matplotlib.pyplot as plt

def rNum():
    return random.random()

def random_scatter(count, range_low, range_high):
    x_vals = [random.randint(range_low,range_high) for i in range(count)]
    y_vals = [random.randint(range_low,range_high) for i in range(count)]
    rcol = [(rNum(), rNum(), rNum()) for i in range(0, count)]
    print(x_vals, y_vals, sep='\n',end='\n\n')
    plt.scatter(x_vals,y_vals, c=rcol)
    plt.show()

for i in range(7):
    plt.xlabel(i**i)
    random_scatter(i**i,0,100)