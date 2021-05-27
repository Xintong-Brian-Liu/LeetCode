'''
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true
'''

# Approach 1 - Brute Force 
# We can store the LinkedList in a list and check if that list is palindrome 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = []
        while head is not None:
            node.append(head.val)
            head = head.next 
        if node == node[::-1]:
            return True
        return False
# Time - O(n) Space - O(n)
'''
In the first part, we're copying a Linked List into an Array List. 
Iterating down a Linked List in sequential order is O(n)O(n), 
and each of the nn writes to the ArrayList is O(1)O(1). 
Therefore, the overall cost is O(n)O(n).

In the second part, we're using the two pointer technique to check whether or not the Array List is a palindrome. 
Each of the nn values in the Array list is accessed once, and a total of O(n/2)O(n/2) comparisons are done. 
Therefore, the overall cost is O(n)O(n). The Python trick (reverse and list comparison as a one liner) is also O(n)O(n).

'''

# Approach 2 - LinkedList manipulation Reserv Second Half in-place
# We can find the second half and reverse it by use two pointer(fast and slow) fast = fast.next.next
# And use two pointer to traverse and compare. 

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous