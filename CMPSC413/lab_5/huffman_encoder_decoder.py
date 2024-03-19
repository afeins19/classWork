from CMPSC413.lab4.priority_queue_array import PriorityQueueArray as Q
from CMPSC413.lab4.base_classes import Comparator, PriorityQueueElement

from CMPSC462.binarySearchTree.binary_search_tree_Redo import BinarySearchTreeNode, build_tree

# getting counts of unique chars in the message, sorted by frequency
def get_unique_char_counts(msg: str) -> dict[(str, int)]:
    unique_chars=dict()

    for char in list(msg):
        char = char.lower() # lower case to reduce complexity

        if char not in unique_chars.keys():
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1

    unique_chars =  dict(sorted(unique_chars.items(), reverse=True)) # sorts the chars by ascending order
    return unique_chars


unique_chars = get_unique_char_counts("AAABBBABBBABBBCCCBABCBABCAABABACBBACBCU")

for char in unique_chars:


 # pq = Q(is_min=True) # initialize a priority queue with elements held in ascending order (smallest is root)
