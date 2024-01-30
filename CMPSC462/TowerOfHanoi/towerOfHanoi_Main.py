class Disk:
    def __init__(self, size):
        self.id = size

    def __repr__(self):
        return f"Disk_{self.id}"


def move(src, tar, pegs):
    """Move  a disk from the source peg to the target peg."""
    disk = src[-1]
    tar.append(disk)
    src.pop()

    # gets the name of our pegs by c
    src_name = [name for name, peg in pegs.items() if peg == src][0]
    tar_name = [name for name, peg in pegs.items() if peg == tar][0]

    print(f" {disk}:  {src_name} >> {tar_name}")


def hanoi(n, src, aux, tar, pegs):
    # base case - we simply move 1 disk from source to target
    if n == 1:
        move(src, tar, pegs) #final trivial move from src to tar
        return


    hanoi(n - 1, src, tar, aux, pegs) #move from src to aux via tar
    move(src, tar, pegs)
    hanoi(n - 1, aux, src, tar, pegs) #move from aux to src via tar


# Initialize the pegs
A = [Disk(3), Disk(2), Disk(1)]
B = []
C = []

pegs = {'A': A, 'B': B, 'C': C}

# Testing the function for 3 disks, moving from peg A to C using B as auxiliary
hanoi(3, A, B, C, pegs)
