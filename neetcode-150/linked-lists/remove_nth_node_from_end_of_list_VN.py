# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #original idea, i still think this might work
        #reverse the list so we can see the end of it
        #using the first node as 1, wait and see if its at the nth node
        #remove the node by connecting it to the next node (need to account for edgecases)
        #re-reverse the list and return it
        #expected TC: O(n), running 3 O(n) algors
        #SC: O(1), therell just be temp vars created
    
        #make a L and R pointer s.t. its n apart (so when R is null, L is where it needs to be)
        #just make sure L is 1 behind actually so that it can assign prev.next to the current.next
        #TC: O(n), you make 1 pass through the LL
        #SC: O(1) for temp vars and dummyHead

        dummyHead = ListNode(0, head)
        left, right = dummyHead, head
        i = 0
        while i < n and right:
            right = right.next
            i += 1

        while right:
            left = left.next 
            right = right.next
        
        left.next = left.next.next
        return dummyHead.next
            


