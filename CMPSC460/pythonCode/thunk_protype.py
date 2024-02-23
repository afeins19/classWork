
# thunkV - function which we will delay
def add1(x):
    return x+1

def main(f):
    x=3 # x=3

    def inner(f):
        x=40
        return f(x)

    return inner(f)

print(main(add1))

