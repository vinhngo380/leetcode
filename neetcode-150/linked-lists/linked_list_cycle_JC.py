class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Tortoise + Hare Situation
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


'''
TLDR: Tortoise + Hare, use slow + fast pointers. When fast eventually catches up to slow, and they equal, then return True. If fast or fast.next == None, then that means there is an end (no cycle).

TC O(n)
SC O(1)
'''
