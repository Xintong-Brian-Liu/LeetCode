'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 

If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

'''

# Approach 1 - Brute Force - 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# We use two loop to traverse two LinkedList and to see if there is pair 
# !! This is exceeding time limit, since we need to repeatly check the LinkedListB 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next

        return None

# Approach 2 - Two Pointers
# We assign two pointers to two LinkedList
# Intersection means that they traverse the same length of path and meet at the end. 
# So when they reach the null, they point to other's head. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next 
        return pa 

# Approach 3 - Hash Table 
# We just store one of the linkedlist into a table
# and iterate another one to see if there is a match

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_in_B = set()
        while headB is not None:
            node_in_B.add(headB)
            headB = headB.next
        while headA is not None:
            if headA in node_in_B:
                return headA
            headA = headA.next
        return None