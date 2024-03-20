import sys
sys.path.append(f'C:\\Users\\aaron\\Projects\\classWork\\CMPSC413\\lab4\\base_classes.py')

PQ_PATH = f'C:\\Users\\aaron\\Projects\\classWork\\CMPSC413\\lab4'
BST_PATH = f'C:\\Users\\aaron\\Projects\\classWork\\CMPSC462\\binarySearchTree\\binary_search_tree_v2.py'

sys.path.append(PQ_PATH)
sys.path.append(BST_PATH)

from CMPSC413.lab4.priority_queue_heap_array import PriorityQueueHeap as PQ
from CMPSC413.lab4.base_classes import Comparator, PriorityQueueElement
from CMPSC413.lab_5.huffman_tree import HuffmanTreeNode
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

def make_huffman_tree_recursive(pq: PQ):
    # base case - prioirty queue contains only one element -> this is the root so return it
    if pq.get_size() == 1:
        return HuffmanTreeNode(data=pq.delete())

    else:
        l_child_data = pq.delete() #self.p, self.v
        r_child_data = pq.delete()
        priority_sum = l_child_data.p + r_child_data.p

        l_child_node = HuffmanTreeNode(data=l_child_data.v, position='0')
        r_child_node = HuffmanTreeNode(data=r_child_data.v, position='1')

        parent = HuffmanTreeNode(
            data=priority_sum,
            l_child=l_child_node,
            r_child=r_child_node
        )
        #print(parent, parent.l_child.data, parent.r_child.data)

        pq.insert(priority=parent.data, value=parent)

        return make_huffman_tree_recursive(pq)

def get_huffman_codes(node, huffman_codes=None, cur_code=''):
    if huffman_codes is None:
        huffman_codes = {}

    if node is None:
        return huffman_codes

    if node:
        print(node.data)


    # leaf node...no children
    if not str(node.data.v).isdigit():
        # base case - leaf node with char
        huffman_codes[node.data.v] = cur_code
        #print(huffman_codes)

    else:
        # rec case - internal node, recurse down the tree
        l_code = cur_code+'0'
        r_code = cur_code+'1'

        print(node.data,v)

        get_huffman_codes(node.data.v.l_child, huffman_codes, l_code)
        get_huffman_codes(node.data.v.data.r_child, huffman_codes, r_code)

    return huffman_codes


TEST_MSG = "AAABBBCCCDDDEEFGADHKASKBVCBACBA"



pq = PQ(is_min=True) # initialize a priority queue with elements held in ascending order (smallest is root)
unique_chars = get_unique_char_counts(TEST_MSG)

# inserting the items into our priority queue
for char, count in unique_chars.items():
    pq.insert(priority=count, value=char)


#rint(pq.pq)
ht_root_node = make_huffman_tree_recursive(pq)
print(get_huffman_codes(node=ht_root_node))

print(type(ht_root_node.data.v))
print(ht_root_node.data.v)
