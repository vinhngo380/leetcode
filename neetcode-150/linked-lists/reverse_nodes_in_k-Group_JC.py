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

        dummy = root = ListNode() # O(n) space due to creating a new list without reversering in-place
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
