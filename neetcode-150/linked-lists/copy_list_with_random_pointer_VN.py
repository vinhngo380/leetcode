"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #map copy to new in a hashmap
        oldToNew = {None: None} 
        current = head
        while current:
            copy = Node(current.val)
            oldToNew[current] = copy
            current = current.next

        #then create pointers
        print(oldToNew)
        current = head
        while current:
            copy = oldToNew[current] 
            copy.next = oldToNew[current.next]
            copy.random = oldToNew[current.random]
            current = current.next

        return oldToNew[head]

'''
TLDR: you can use a hashmap to correspond with the copy and the original
so first pass is to create the hashmap and the second pass is to create the connections in the LL
TC: O(n) since you are only going over the list twice
SC: O(n) since you need to make a new list/the dict size is as big as the original list
'''
