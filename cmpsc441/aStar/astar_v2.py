import math
from queue import PriorityQueue
import copy
class Node:
    def __init__(self, vals: [], parent=None, g_val=0, h_val=0):
        # generating an sqrt(n) by sqrt(n) puzzle
        self.puzzle = [vals[i:i + int(math.sqrt(len(vals)))] for i in range(0, len(vals), int(math.sqrt(len(vals))))]

        # values in puzzle
        self.vals = vals

        #cost functions
        self.g_val = g_val
        self.h_val = h_val
        self.f_val = self.g_val + self.h_val

        # parent node
        self.parent = parent

    def val_pos(self, val):
        """get the position of a value within the puzzle"""
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == val:
                    return i, j

    def empty_space_pos(self):
        """get the position of 0 in the puzzle"""
        return self.val_pos(0)

    def possible_moves(self):
        """finds all possible moves for a given node"""
        r_cur, c_cur = self.empty_space_pos()

        moves = []
        if r_cur > 0:
            moves.append((r_cur - 1, c_cur))
        if r_cur < len(self.puzzle) - 1:
            moves.append((r_cur + 1, c_cur))
        if c_cur > 0:
            moves.append((r_cur, c_cur - 1))
        if c_cur < len(self.puzzle[0]) - 1:
            moves.append((r_cur, c_cur + 1))

        return moves

    def make_move(self, r, c):
        """apply a move (swapping 0 and the value in the position 0 is being moved to)"""
        r_empty, c_empty = self.empty_space_pos()

        self.puzzle[r_empty][c_empty], self.puzzle[r][c] = self.puzzle[r][c], self.puzzle[r_empty][c_empty]

        # Update vals after the move
        self.vals = []
        for row in self.puzzle:
            for num in row:
                self.vals.append(num)

    def __str__(self):
        "string representation of the node (using the puzzle in this case)"
        return "\n".join(["  ".join(map(str, row)) for row in self.puzzle])

    def __lt__(self, other):
        """less than comparison for the node"""
        return self.f_val < other.f_val

    def __eq__(self, other):
        """equality comparison for the node"""
        return isinstance(other, Node) and self.puzzle == other.puzzle

    def __hash__(self):
        """returns a unique has for the string to be used in the priority queue"""
        return hash(str(self.puzzle))

class AStar:
    def __init__(self, initial_node: Node, goal_node: Node):
        self.i_node = initial_node
        self.g_node = goal_node

        self.open = PriorityQueue()
        self.open.put(initial_node)
        self.closed = set()

    def manhattan(self, n: Node):
        """finds the sum of all manhattan distance from the current node to goal"""
        m_dist = 0
        for val in range(1, len(n.vals)):  # Excluding 0
            x_cur, y_cur = n.val_pos(val)
            x_g, y_g = self.g_node.val_pos(val)
            m_dist += abs(x_cur - x_g) + abs(y_cur - y_g)
        return m_dist

    def generate_children(self, n: Node):
        """generates all possible child nodes from a given state"""
        children = []
        for move in n.possible_moves():
            r, c = move
            child_vals = copy.deepcopy(n.vals)  # Deep copy of vals
            child = Node(vals=child_vals, parent=n, g_val=n.g_val + 1)
            child.make_move(r, c)
            child.h_val = self.manhattan(child)
            child.f_val = child.g_val + child.h_val
            children.append(child)
        return children

    def search(self):
        """A* search algorithm
            - similar to uniform cost
        """
        while not self.open.empty():
            cur_node: Node = self.open.get()

            # comparing nodes with the equality override we specified in the node class
            if cur_node == self.g_node:
                path = []

                # gives us the solution in start -> goal order
                while cur_node:
                    path.append(cur_node)
                    cur_node = cur_node.parent
                return path[::-1]

            # add the node to visited list
            self.closed.add(cur_node)

            # makes children from current node and adds them if not yet visisted
            for child in self.generate_children(cur_node):
                if child not in self.closed and child not in self.open.queue:
                    self.open.put(child)
        return None

    def __str__(self):
        out=""
        i=1
        for node in self.search():
            n_hash = str([node.puzzle])
            out+="("+str(i)+", Node: "+n_hash + " )"  + " -> "
            i+=1
        return out.rstrip(" -> ")

# Example
goal_vals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
initial_vals = [1,2,3,4,5,6,7,8,9,10,0,11,13,14,15,12]

initial_node = Node(vals=initial_vals)
goal_node = Node(vals=goal_vals)

astar_solver = AStar(initial_node=initial_node, goal_node=goal_node)
solution_path = astar_solver.search()
print(astar_solver)

# Print solution path
if solution_path:
    i=1
    for node in solution_path:
        print("step: "+str(i))
        print(node)
        print("".join(["----" for i in range(len(node.puzzle[0]))]))
        i+=1
else:
    print("No solution found!")
