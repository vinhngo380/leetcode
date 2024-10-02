class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Below is TC O(n), SC O(n).
        '''
        tempArr = [] # SC O(n)
        while head is not None:
            tempArr.append(head.val)
            head = head.next
        tempArr.reverse() # TC O(n)

        dummy = root = ListNode() # SC O(n)
        for a in tempArr: # TC O(n)
            root.next = ListNode(a)
            root = root.next
        return dummy.next
        '''

        # Can we do in SC O(1) while maintaining TC O(n)?
        curr = head
        prev = None
        while curr is not None: # TC O(n)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

'''
TLDR: Use a two-pointer approach (curr and prev) and set curr.next to prev while maintaining a temp variable to keep track of the next element in Linked List.

TC O(n)
SC O(1), reversing in place.
'''
