# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #similar to remove nth node, make a right pointer
        #that is k far, then reverse up to k
        #when left = right, move right forwards k times and so on
        #TC: O(n) since wed only be going through the LL once
        #SC: O(1), we are modifiying the original LL w/o anything else

        #as of 10/7 this algor is not correct!
        dummyHead = ListNode(0, head)
        prev, right = dummyHead, head
        n = 0
        while True:
            nextGroup = None
            while n < k:
                if not right:
                    break
                right = right.next
                nextGroup = right.next
                n += 1
            
            prev, current = right, prev.next
            while current != nextGroup:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            n = 0

            temp = prev.next
            prev.next = right
            prev = temp
        return prev
            
