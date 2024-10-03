# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        result = dummyHead
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = ListNode(list1.val)
                list1 = list1.next
            elif list2.val < list1.val:
                result.next = ListNode(list2.val)
                list2 = list2.next
            result = result.next

        if list1:
            result.next = list1   
        if list2:
            result.next = list2   
        return dummyHead.next

'''TLDR
make a resulting LL then:
    look at the first value of each LL, whichever one is less
    add it to the resulting LL and only move that list
    keep going until one of the LL run out

at the very end, add the other LL if there are remaining elements 

runtime: O(n) -- we're only iterating through the LLs once
SC: O(n) -- itll be a new list that uses both LLs lengths 
'''

