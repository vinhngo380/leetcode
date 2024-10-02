class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = root = ListNode() # SC O(n + m)
        while list1 and list2: # O(n) if n > m or O(m) if n < m
            if list1.val <= list2.val:
                root.next = ListNode(list1.val)
                list1 = list1.next
            else:
                root.next = ListNode(list2.val)
                list2 = list2.next
            root = root.next
        
        # Goes through the rest
        while list1:
            root.next = ListNode(list1.val)
            list1 = list1.next
            root = root.next
        while list2:
            root.next = ListNode(list2.val)
            list2 = list2.next
            root = root.next

        return dummy.next

'''
TLDR: Iter up through both lists until we reach the end of a LL. Then we iterate through the rest of the other, linking it to the root.

TC O(n+m), have to go through both resulting in combined times.
SC O(n+m), have to have a new LL, resulting in combined lengths.
'''
