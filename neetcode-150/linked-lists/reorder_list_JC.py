class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next

        l, r = 1, len(arr) - 1
        while l <= r:
            head.next = ListNode(arr[r])
            head = head.next
            if l != r:
                head.next = ListNode(arr[l])
                head = head.next
            l += 1
            r -= 1
'''
TLDR: Use two pointer approach here, first by converting the LL to an arr. Then we move incremently inwards until l <= r (important for LL with even lengths).
We have a conditional l != r to avoid duplicate values.

TC O(n)
SC O(n) due to array usage. Could be O(1), but significantly more code with slow/fast pointers.
'''

