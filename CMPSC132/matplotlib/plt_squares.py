import matplotlib.pyplot as plt
import random

def rNum():
    return random.random()

values = list(range(1,100))
squares = [v*v for v in values]
rcol=[(rNum(),rNum(),rNum()) for i in range(1,100)]


plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Square of Value",fontsize=12)
plt.tick_params(axis='both', labelsize=14)

plt.axis([0,100,0,11000])

plt.scatter(values, squares, s=10, c=(rcol))


plt.show()
