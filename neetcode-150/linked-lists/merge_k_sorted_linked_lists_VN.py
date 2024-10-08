# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #put all the heads into a dictionary (0->n-1)
        #go through the list and see which one is the least
        #save the key in a var
        #if a LL is empty, skip it
        dummyHead = ListNode(0)
        isEmpty, keyLowest, lowestVal = False, -1, None
        LLMapper = {}
        for i, head in enumerate(lists):
            LLMapper[i] = head
        print(LLMapper)
        
        curr = dummyHead
        while lowestVal != float('inf'):
            keyLowest = -1
            lowestVal = float('inf')
            for key, head in LLMapper.items():
                if head and head.val < lowestVal:
                    keyLowest = key
                    lowestVal = head.val
            if keyLowest == -1:
                break
            curr.next = LLMapper[keyLowest]
            LLMapper[keyLowest] = LLMapper[keyLowest].next
            curr = curr.next
        return dummyHead.next

'''TLDR
TC: O(n^2)
SC: O(n^2)

'''
