class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use a fast and slow pointer to find a cycle
        #called floyd's algor or tortoise and hare
        #when you find an intersection go from the start
        #and see where it intersects again
        #TC: O(n), at worst the slow pointer will iterate O(n) times
        #SC: O(1), only using pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

#not really sure why my other code doesnt work tbh, but neetcode does
