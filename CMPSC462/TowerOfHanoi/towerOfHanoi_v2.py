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
        self.disks = []
        self.size = len(self.disks)

    def add_disk(self, disk: Disk):
        self.disks.append(disk)

    def pop_disk(self):
        return self.disks.pop()

    def __sizeof__(self):
        return len(self.disks)

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
    if n == 1:
        tar.add_disk(src.pop_disk())
        print_state(src, aux, tar)
        return

    hanoi_recursive(n-1, src, tar, aux)
    tar.add_disk(src.pop_disk())

    print_state(src, aux, tar)

    hanoi_recursive(n-1, aux, src, tar)

def hanoi_iterative(src, aux, tar):
    """Algorithm:
        - total possible moves is 2^n - 1 for n disks

        Possible Moves for any scenario:
            1. One Pole has no disks:
                move a disk from non-empty pole to empty pole
            2. A pole has a top disk thats smaller than another's:
                move the SMALLER disk to pole with larger disk
    """

    start_size = src.__sizeof__()
    total_moves = 2**start_size - 1

    for i in range(total_moves):
        if i%3 == 1: # move src -> dest directly (trivial move)
            tar.add_disk(src.pop_disk())
            print_state(src, aux, tar)

        elif i%3 == 2: # move src -> aux pole
            aux.add_disk(src.pop_disk())

        elif i%3 == 1:
            tar.add_disk(aux.pop_disk()) #move from aux -> destination

A = Peg('A')
B = Peg('B')
C = Peg('C')

A.disks = [Disk(i) for i in range(5,0,-1)]
B.disks = []
C.disks = []

# recursive algorithm
print_state(A, B, C)
hanoi_recursive(5, A, B, C)


# iterative algorithm
print_state(A, B, C)
hanoi_iterative(A,B,C)