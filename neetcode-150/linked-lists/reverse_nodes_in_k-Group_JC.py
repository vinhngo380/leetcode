class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Can we first try a O(n) space solution?
        temp = []
        tempNode = head
        length = 0
        # First loop to find len of LL to get total groups
        while tempNode is not None:
            tempNode = tempNode.next
            length += 1

        groups = length // k
        currGroups = 0

        dummy = root = ListNode() # O(n) space due to creating a new list without reversing in-place
        while head is not None:
            while len(temp) < k and head is not None:
                temp.append(head)
                head = head.next
            while len(temp) > 0 and currGroups < groups:
                currNode = temp.pop()
                root.next = currNode
                root = root.next
            currGroups += 1

        for i in range(len(temp)):
            root.next = temp[i]
            root = root.next

        root.next = None

        return dummy.next

'''
TLDR: Get the num of groups by first using a loop to iterate through, then floor div by k to get available groups. Then, using another loop, we use a temp arr (stack) to reverse the nodes.
Finally, we iterate through the remaining in temp (if any), set root.next to None (to avoid cycles), and return our dummy.next. By using the dummy, it means that we have created a
NEW list. This means it is in O(n) space. It is possible to do it in O(1) (the follow-up) by reversing in place, perhaps with a counter.

TC O(n)
SC O(n)
'''
