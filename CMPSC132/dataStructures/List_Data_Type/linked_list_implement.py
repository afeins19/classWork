'''linked list is a list with the items are connected by an explicit link...you can not just access an item directly
the unordered list is simply a collection of nodes... We need only know the explicit location of the head and the fact
that nothing succeeds the last item. the UnorderedList class must maintain a reference to the first node.

The head must point to the first item in the list

'''

'''a node holds a value as well as a reference to the next item'''
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

class LinkedList:

    def __init__(self):
        self.head = None #head always points to the first item in the collection

    def add(self, item): #creates a node and sets the head
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    #compares each node's data field to the search query
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData == item:
                found = True

            else:
                current = current.getNext()

        return found

    def traverse(self):
        output=""
        current = self.head
        while current != None:
            output = output + ' ' + str(current.getData())
            current=current.getNext()

        return output

    #todo implement this!!!!!!!!!!!!!!!!!!!!!
    def remove(self, item):
        current = self.head
        prev = None

        while current != None:
            if current == item:
                if prev == None:
                    self.head = current.getNext()
                    break
                prev.next = current.getNext()

            else:
                prev=current
                current = current.getNext()

    def __str__(self):
        current = self.head
        outString=''

        while current!=None:
            outString = outString +', '+ str(current.getData())
            current=current.getNext()
        return '['+outString+']'







myList = LinkedList()

myList.add(22)
myList.add(69)
myList.add(420)
print(myList.search(33))
myList.remove(22)

myList.traverse()
myList.remove(69)
print(myList.__str__())

print(myList)


