class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self): #returns the item at this node
        return self.data

    def getNext(self): #gets the item which this node points to
        return self.next

    def setData(self,newdata): #sets an item to this node
        self.data = newdata

    def setNext(self,newnext): #changes the pointer location of this node
        self.next = newnext

    def __str__(self):
        return str(self.getData())


#using recursion here:
def getLength(node):
    #base case:
    if node == None:
        return 0
    else:
        return 1 + getLength(node.getNext())


#generate nodes here
def createNodes(count):
    n = [Node(i) for i in range(count)]
    for i in range(count-1):
        n[i].setNext(n[i+1])
    return n[0]

print(getLength(createNodes(100)))