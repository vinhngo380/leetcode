class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        length = 1
        while fast.next is not None: # Get Length of LL
            length += 1
            fast = fast.next

        if length == n: # If length == n, remove head
            return head.next

        diff = length - n - 1  
        for i in range(diff): # Gets the Node right before Nth Node to Be Removed.
            slow = slow.next
        if slow.next and slow.next.next: # If Node, (x) Node, Node.
            slow.next = slow.next.next
        elif slow.next: # If another Node, we remove that.
            slow.next = None
        else: # No other Nodes, set head to None.
            head = None

        return head

  '''
  TLDR: Use fast and slow pointers - fast for getting the LL length, and slow for identifying the node prior to the one being removed. 
  Note that there are 4 test cases we can check for:
    1. Length == N: remove the first node, head = head.next
    2. Valid (3+ Nodes): remove the middle node between two, slow.next = slow.next.next
    3. Two nodes: remove the second node by setting slow.next = None
    4. Only 1 Node: remove that node by setting head = None

  TC O(n)
  SC O(1)
  '''
