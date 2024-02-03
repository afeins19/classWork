# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2: 
            return list1

        # determine the head 
        head = ListNode()
        out = head 

        while list1 and list2: # l1 is "empty"

            # compare vals 
            if list1.val < list2.val: # v1 < v2
                head.next = list1
                list1 = list1.next 
            else:                   # v1 <= v2
                head.next = list2
                list2 = list2.next 

            head = head.next 

        head.next = list1 if list1 else list2 # append list with remaining elements 
       
        return out.next
  
