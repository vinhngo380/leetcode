# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #find whichever one is less, add that to the new list
        #if one of the lists dont have elements anymore, just add the
        #rest on the new list
        #TC: O(n) you have to go through 2 lists of O(n) size
        #SC: O(1) you just make a dummyhead node
        dummyHead = ListNode(0)
        current = dummyHead
        while list1 and list2:
            if list1.val <= list2.val:
               current.next = list1
               list1 = list1.next
            else:
               current.next = list2 
               list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummyHead.nex
