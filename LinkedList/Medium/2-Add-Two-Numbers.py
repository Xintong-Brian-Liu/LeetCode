'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

'''

# Approach 1 - Elementary Math
# Use divmod(num1, num2) = (quo, remaining) (8,3) = (2,2) 
# carry, rem = (num1, 10)
# 7 / 10 = 0 ... 7


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = node = ListNode(0)
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, rem = divmod(carry + val1 + val2, 10)
            node.next = rem
            node = node.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None # Make sure .next does not apply to None
        return res.next
#!! 遇到linkedlist的这种需要新建list的题目，我们用一个pointer去走，然后保留一个在head，最后return head.next
