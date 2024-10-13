#use left and right pointers -- left for first unique val and right to skip 
#through until a new unique val is found
#TC: O(n) :)
#SC: O(1) :)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        left = right = head 
        if not head:
            return None

        while right:
            if left.val == right.val:
                right = right.next
            else:
                left.next = right
                left = left.next
                right = left
        left.next = None
        return dummyHead.next
