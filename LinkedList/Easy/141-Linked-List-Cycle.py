'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''
# Approach 1  Floyd's Cycle Finding Algorithm 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        slow = fast = head 
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next 
            if fast == slow:
                return True
        return False
'''
Time complexity : O(n)O(n). Let us denote nn as the total number of nodes in the linked list. 
To analyze its time complexity, we consider the following two cases separately.

Space complexity : O(1)O(1). We only use two nodes (slow and fast) so the space complexity is O(1)O(1).

'''

# Appeoach 2 - Hash Table 
# We save all the node in a table and check if it is in the table

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()
        while head is not None:
            if head in nodes:
                return True 
            nodes.add(head)
            head = head.next 
        return False
'''
Time complexity : O(n)O(n). We visit each of the nn elements in the list at most once. 
Adding a node to the hash table costs only O(1)O(1) time.

Space complexity: O(n)O(n). The space depends on the number of elements added to the hash table, which contains at most nn elements.
'''