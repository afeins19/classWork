import time

def cyber_print(text):
    for i in text:
        print(i,end='')
        time.sleep(.205)

cyber_print('Welcome to the cyber text module that i just made!')