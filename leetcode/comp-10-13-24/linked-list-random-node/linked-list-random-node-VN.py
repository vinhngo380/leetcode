# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.all_nums = set()
        current = head
        while current:
            if current.val not in self.all_nums:
                self.all_nums.add(current.val)
            current = current.next

    def getRandom(self) -> int:
        return random.choice(list(self.all_nums))
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
#not finished code
