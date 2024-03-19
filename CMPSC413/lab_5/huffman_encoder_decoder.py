import sys
sys.path.append(f'C:\\Users\\aaron\\Projects\\classWork\\CMPSC413\\lab4\\base_classes.py')

PQ_PATH = f'C:\\Users\\aaron\\Projects\\classWork\\CMPSC413\\lab4'
BST_PATH = f'C:\\Users\\aaron\\Projects\\classWork\\CMPSC462\\binarySearchTree\\binary_search_tree_v2.py'

sys.path.append(PQ_PATH)
sys.path.append(BST_PATH)

from CMPSC413.lab4.priority_queue_array import PriorityQueueArray as PQ
from CMPSC413.lab4.base_classes import Comparator, PriorityQueueElement
from CMPSC413.lab_5.binary_tree import HuffmanTreeNode
from CMPSC462.binarySearchTree.binary_search_tree_v2 import BinarySearchTreeNode, build_tree

# getting counts of unique chars in the message, sorted by frequency
def get_unique_char_counts(msg: str) -> dict[(str, int)]:
    unique_chars=dict()

    for char in list(msg):
        #char = char.lower() # lower case to reduce complexity

        if char not in unique_chars.keys():
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1

    return unique_chars


def make_huffman_tree(pq :PQ) -> HuffmanTreeNode:
    parents = []

    # huffman algorithm for the huffman tree
    while len(pq.pq) > 1:
        l_child = HuffmanTreeNode(data=pq.delete(), position='0')
        r_child = HuffmanTreeNode(data=pq.delete(), position='1')


        parent = HuffmanTreeNode(
            data = sum(l_child.data.p, r_child.data.p),
            l_child = l_child,
            r_child = r_child)

        parents.append(parent)










TEST_MSG = "AACABBEECBBABCCBAAABCBABCCCBACBECBABCEBCBE"



pq = PQ(is_min=True) # initialize a priority queue with elements held in ascending order (smallest is root)
unique_chars = get_unique_char_counts(TEST_MSG)


# inserting the items into our priority queue
for char, count in unique_chars.items():
    pq.insert(priority=count, value=char)



# print(sorted(unique_chars.items(), key=lambda x: x[1]))
# print(pq.peek())

