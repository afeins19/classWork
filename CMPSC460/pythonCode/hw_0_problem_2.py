# return a sorted list of integers based on operator
# less than < ascending
# greater than > descending

def merge_up(l1, l2):
    # base case
    if len(l1) == 1 and len(l2) == 1: # list is reduced to the two items well compare
        if l1[0] < l2[0]: # item in l1 is less than item in l2...return [l1, l2]
            return [l1[0], l2[0]]

        else:
            return [l2[0], l1[0]]

    # recursive case: return starting items and then the rest of the list?
    return merge_up([l1[0]], [l2[0]]) + merge_up(l1[1:], l2[1:])

def merge_down(l1, l2):
    # base case
    if len(l1) == 1 and len(l2) == 1:
        if l1[0] > l2[0]:
            return [l1[0], l2[0]]
        return [l2[0], l1[0]]

    return merge_down([l1[0]], [l2[0]]) + merge_down(l1[1:], l2[1:])

print(merge_up([1,4,6],[2,5,8]))
print(merge_down([6,4,1], [8,5,2]))


