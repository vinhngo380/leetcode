# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
#TLDR using floyd's cycle detection method, but if there's no cycle,
#then fast values will be null first
#TC: O(n) you have to go through the LL at worst 
#SC: O(1) since only 2 vars are use
