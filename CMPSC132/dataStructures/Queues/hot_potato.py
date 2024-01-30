'''Implementation of the Queue data structure'''

from Data_Structures.Queues.Queue_Implement import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>=2:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

myList=['mark','jeff','simon','rita','cliff']

print(hotPotato(myList, 3))







