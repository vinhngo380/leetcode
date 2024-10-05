# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #find the "midway" section of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse 2nd list
        secondList = slow.next
        prev = slow.next = None
        while secondList: 
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp

        #merge lists together
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


'''TLDR
since we're going to be alternating between the last and first nodes, it means
that the first half will be going forwards and the second going backwards

so you find that using fast-slow pointers and then reverse the second half

then merge the two lists together going "forwards"

TC: O(n) since youre going iterating through the list seqeuenctically
SC: O(1) since youre only using temp vars and are not creating new lists
'''
