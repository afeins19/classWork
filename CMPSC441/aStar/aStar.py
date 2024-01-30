


"""todo
    - implement a class to represent our puzzle table
        - init(dimension)
        - manhatten()
"""
import random
import math

class Node:
    def __init__(self,  vals: [], parent=None, g_val=0, h_val=0):
        """create a 2D array to represent the table of values [0...dim]"""
        self.p_size = len(vals) + 1
        self.p_dim = int(math.sqrt(self.p_size))
        self.vals = vals
        self.puzzle = [self.vals[i:i+self.p_dim] for i in range(0, self.p_size-1, self.p_dim)]

        #heuristic function values
        self.g_val = 0
        self.h_val = 0
        self.f_val = 0

        #parent node
        self.parent = None

    def val_pos(self, val):
        for i in range(self.p_dim):
            for j in range(self.p_dim):
                if self.puzzle[i][j] == val:
                    return (i,j)

    def empty_space_pos(self):
        return self.val_pos(0)

    def possible_moves(self):
        """returns a list of possible moves in each direction"""
        x,y = self.empty_space_pos()

        moves = {'row':[], 'col':[]}
        out = []

        if x > 0:
            moves['row'].append(x-1)

        if x < self.p_dim-1:
            moves['row'].append(x+1)

        if y > 0:
            moves['col'].append(x-1)

        if y < self.p_dim-1:
            moves['col'].append(x+1)

        out = [(r,0) for r in moves['row']]
        out+= [(0,c) for c in moves['col']]

        return out

    def make_move(self, r,c):
        temp = self.puzzle[r][c]
        z_r, z_c=self.empty_space_pos()
        self.puzzle[r][c] = 0
        self.puzzle[z_r][z_c] = temp
    def __str__(self):
        out = ""
        for row in self.puzzle:
            out+="\n"+str(row)
        return out

class AStar:
    def __init__(self, initial_node: Node, goal_node: Node):
        self.i_node = initial_node
        self.g_node = goal_node

    def manhatten(self, n: Node):
        """finds the sum of manhatten distances between the current node and the goal node"""
        m_dist = 0
        for val in n.vals:
            x_cur, y_cur = n.val_pos(val)
            x_g, y_g = self.g_node.val_pos(val)
            m_dist += abs(x_cur - x_g) + abs(y_cur - y_g)
        return m_dist

    def generate_children(self, n: Node):
        children = []
        for move in n.possible_moves():
            child=Node(parent=n, vals=n.vals, g_val=n.g_val+1, h_val=self.manhatten(n))
            r,c=move

            child.make_move(r,c)
            children.append(child)
        return children

a = Node(vals=[1,2,0,3,4,5,7,6,8])
b= Node([8,6,0,3,4,5,7,1,2])

search = AStar(a,a)
search.manhatten(b)
print(a)
print(a.possible_moves())
k=search.generate_children(a)
print(k[0].puzzle, k[1].puzzle)



