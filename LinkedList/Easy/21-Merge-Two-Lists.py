'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Input: 
1 -> 2 -> 4
1 -> 3 -> 4

Basic Logic:
1. Start a new linkedList with two cursor, one to keep reference on the head, one to add value. 
2. Whoever is smaller get inserted into the list curr.next = l1 or l2
3. curr = curr.next 
4. 

ListNode(0) -> None
curr/head

1 == 1

ListNode(0) ->   1    -> 
head            curr

1 < 3

ListNode(0) ->   1    ->    1       ->
head                        curr

2 < 3 

ListNode(0) ->   1    ->    1       ->      2       ->      
head                                        curr

4 > 3 

ListNode(0) ->   1    ->    1       ->      2       ->      4       ->  
head                                                        curr

4 == 4

ListNode(0) ->   1    ->    1       ->      2       ->      4       ->      4
head                                                                        curr

Return head.next 
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = curr = ListNode(-1) # Start a new linkedList, use curr as cursor to add value
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 # Point curr.next to l1
                l1 = l1.next
            else:
                curr.next = l2 
                l2 = l2.next 
            curr = curr.next # Move the curr to current number
        curr.next = l1 or l2
        return prehead.next

'''
Time complexity : O(n + m)O(n+m)

Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. 
All other work is constant, so the overall complexity is linear.

Space complexity : O(1)O(1)

The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.

'''