"""Uses of Doubly Linked Lists:

    these differ from singly linked lists because each node now stores a pointer to the previous node in the chain.
    This makes traversal more efficient since we only need to keep track of the current node as the current node has a
    reference to the previous one.

    Uses for doubly linked lists:

    1. Text Editor: a doubly linked list can be used to create a text editing program. Each node is a charecter
    in am instance of the text editor. The cursor position may be next to any given charecter and may move forward or backwards.
    The cursor will know where to move from any given charecter as each one will always point back or forward to its neighbor

    2. Dynamic memory: we can efficiently implement a memory management system with the use of doubly linked-lists. Memory
    Blocks can change as required by some operating system or allocator and hubs will be the programs uing those memory blocks.
    when a program frees up some memory, it may be allocated to another program efficiently.

    3. Polynomial Representation Program: we can efficiently represent polynomial expressions with doubly linked lists.
    Each term in the polynomial expression is a node and it will keep track of its position relative to its right and left
    neighbor.
"""
class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if not self.head:
            self.head = node(data)
            self.tail = self.head

        else:
            new_node = node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def find_node(self, data):
        curr = self.head

        while curr and not curr.data == data:
            curr = curr.next

        return curr

    def delete(self, data):
        temp = self.find_node(data)

        if temp:
            if temp.prev:
                temp.prev.next = temp.next
            else:
                self.head = temp.next  # Update head if deleting the head

            if temp.next:
                temp.next.prev = temp.prev
            else:
                self.tail = temp.prev  # Update tail if deleting the

    def reverse(self):
        temp = None # swap place holder
        current = self.head


        while current:
            temp = current.prev # hold position of previous node
            current.prev, current.next = current.next, temp # swap prev and next of current node

            current = current.prev # move to next node in the chain but by using the prev (since we swapped)

        # make the head the previous tail
        if temp:
            self.head = temp.prev

    def start_insert(self, data):
        if self.head:
            temp_head = self.head

            # creating a new node with the data passed in
            head = node(data)

            temp_head.prev = head # pointing back to the new head

            self.head = head # setting this new node as the head
            self.head.next = temp_head # pointing it to the previous head
            self.head.prev = None
        else:
            return

    def middle_insert(self, data, insert_before): # specify what node to insert this one before
        insert_location = self.find_node(insert_before) # traversing the linked list until we find the right node

        if insert_location:  # making sure that node exists
            insertion = node(data)  # creating the new node

            temp_prev = insert_location.prev
            temp_prev.next = insertion
            insertion.prev = temp_prev  # point back from the new node to the one we are replacing in its position
            insertion.next = insert_location  # set our new node to point to the one we are inserting before

            insert_location.prev = insertion  # point back from the node we are inserting before

        else:
            return

    def end_insert(self, data):
        # finding the end of our linked list
        curr = self.head

        while curr:
            curr = curr.next

        if curr:
            # found the tail, now we point it to a new node
            insertion = node(data)
            curr.next = insertion # point the previous tail to our node
            insertion.prev = curr # point the new node back to the old tail
        else:
            return


test = DoubleyLinkedList()
for i in range(1,5):
    test.append(i)

print("Original Linked List (doubly):")
test.traverse()

test.start_insert(0)
print("Inserting at the start")
test.traverse()

print("\nInserting in the middle (between 2 and 3)")
test.middle_insert(2.5, insert_before=3)
test.traverse()

print("\nInserting at the end (value of 11)")
test.end_insert(6)
test.traverse()

print("\nReversal: ")
test.reverse()
test.traverse()