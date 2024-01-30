from Queue import Queue
class Stack:
    def __init__(self):
        self.stack = list()
    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[self.size()-1]
        return None

    def __repr__(self):
        return str(self.stack)

class Queue:
    def __init__(self):
        self.queue = list()
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def __repr__(self):
        return self.queue

class Deque:
    def __init__(self):
        self.deque = Queue()

    def enqueue(self, item):
        self.deque.enqueue(item)

    def deque(self):
        self.deque.dequeue()

    def isEmpty(self):
        return self.deque.size() == 0

    def size(self):
        return self.deque.size()

"""Objects:
    - Disk
        - size: int

    - Peg
        - name: str
        - disks: list of Disk

    Algorithm:
    Hanoi
"""

class Disk:
    def __init__(self,size):
        self.size = size

    def __repr__(self):
        return "".join(["*" for i in range(self.size)])


class Peg:
    def __init__(self, name: str):
        self.name = name
        self.disks = Stack()
        self.size = self.disks.size()

    def add_disk(self, disk: Disk):
        self.disks.push(disk)

    def pop_disk(self):
        return self.disks.pop()

    def __sizeof__(self):
        return self.disks.size()

    def __str__(self):
        return str(self.disks)

def print_state(src, aux, tar):
    print("Source: "+str(src))
    print("Aux: "+str(aux))
    print("Target: "+str(tar))
    print("\n")

def hanoi_recursive(n, src, aux, tar):
    """
           Algorithm:

           1. create frames for each function calls until we reach n=1 disks
           2. perform the move souce peg -> target peg
           3. move n-1 pegs from source to aux
           4. move n-1 peg from aux to target
           5. goto 1
       """
    # trivial move from src -> tar
    if n == 1:
        tar.add_disk(src.pop_disk())
        print_state(src, aux, tar)
        return

    # create recursion frames for all disks from n to n-1
    hanoi_recursive(n-1, src, tar, aux)

    #function returns here when the first round of recursive calls completes
    tar.add_disk(src.pop_disk()) # adding a disk to the aux peg
    print_state(src, aux, tar)
    hanoi_recursive(n-1, aux, src, tar)  # for each recursive frame, we move all disks that were placed in aux -> tar

def move_disk(src, tar):
    """Algorithm:
           - total possible moves is 2^n - 1 for n disks

           Possible Moves for any scenario:
               1. One Pole has no disks:
                   move a disk from non-empty pole to empty pole
               2. A pole has a top disk thats smaller than another's:
                   move the SMALLER disk to pole with larger disk

        Problems Encountered:
            - we need to check if our stacks are empty before we attempt a pop

       """
    if not src.disks.is_empty() or not tar.disks.is_empty():  # case 1: a peg has no disks
        if src.disks.is_empty():
            src.add_disk(tar.pop_disk())
        elif tar.disks.is_empty():
            tar.add_disk(src.pop_disk())
        else:  # case 2: atleast 2 pegs have disks
            if src.disks.peek().size > tar.disks.peek().size:
                src.add_disk(tar.pop_disk())
            else:
                tar.add_disk(src.pop_disk())

def hanoi_iterative(n, src, aux, tar):
    if n % 2 == 0:  # case for even number of disks: the first move we make is from src -> aux
        aux, tar = tar, aux

    total_moves = 2**n - 1

    for i in range(total_moves):
        if i % 3 == 0: # we have some multiple of 3 moves
            move_disk(src, tar)
        elif i % 3 == 1:
            move_disk(src, aux)
        elif i % 3 == 2:
            move_disk(aux, tar)

        print_state(src, aux, tar)

"""Iterative Demonstration: """
# Creating pegs
src_peg = Peg("Source")
aux_peg = Peg("Auxiliary")
tar_peg = Peg("Target")

# Add 3 disks to the src_peg
src_peg.add_disk(Disk(3))
src_peg.add_disk(Disk(2))
src_peg.add_disk(Disk(1))

# Print the initial state
print("\nInitial State:\n")
print_state(src_peg, aux_peg, tar_peg)

# Apply the iterative solution
hanoi_iterative(3, src_peg, aux_peg, tar_peg)

print("\n--------------------------------")

"""Recursive Demonstration: """
# Creating pegs
src_peg = Peg("Source")
aux_peg = Peg("Auxiliary")
tar_peg = Peg("Target")

# Add 3 disks to the src_peg
src_peg.add_disk(Disk(3))
src_peg.add_disk(Disk(2))
src_peg.add_disk(Disk(1))

# Print the initial state
print("\nInitial State:\n")
print_state(src_peg, aux_peg, tar_peg)
hanoi_iterative(3, src_peg, aux_peg, tar_peg)


"""Real-Life Scenario: Airport"""

departures = Queue()

departures.enqueue("American 572")
departures.enqueue("Delta 891")
departures.enqueue("Jet Blue 202")

arrivals = Queue()
arrivals.enqueue("Air Canada 5")

for departure in departures.queue:
    if not arrivals.is_empty():
        landing_aircraft = arrivals.dequeue()
        print("Waiting for: "+landing_aircraft+" to land...\n")
    print(departure+" is departing...")





