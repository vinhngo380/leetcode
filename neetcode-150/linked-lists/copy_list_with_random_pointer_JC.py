class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # NOTE THAT NODE.RANDOM is a NODE, not INTEGER.

        nodeMap = dict()
        temp = head
        dummy = root = Node(0) # Beginning of new LL

        while temp is not None: # TC O(n)
            root.next = Node(temp.val)
            nodeMap[temp] = root.next # Interesting to note that we can use the Nodes themselves as keys due to their hashability.
            root = root.next
            temp = temp.next

        dummy = dummy.next
        dummyTemp = dummy
        while head is not None: # TC O(n)
            if head.random:
                dummyTemp.random = nodeMap[head.random]
            head = head.next
            dummyTemp = dummyTemp.next
            
        return dummy

'''
TLDR: Use a dictionary to keep track of each node, mapping node -> node. This allows for TC O(1) lookup time (rather than going through the LL again), but uses O(n) space.

TC O(n+n) = O(n)
SC O(n) due to hashMap.
'''
