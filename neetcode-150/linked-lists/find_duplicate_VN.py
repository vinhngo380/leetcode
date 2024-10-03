class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, slow_temp, fast = 0, 0, nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        while slow != slow_temp:
            slow_temp = nums[slow_temp]
            slow = nums[slow]
        
        return slow

#first solution
# found_nums = set()
# for num in nums:
#     if num in found_nums:
#         return num
#     found_nums.add(num)
#TC: O(n) -- finding something in a set is O(1) so at worst the duplicate is at the end
#SC: O(n) -- the set can be O(n) b/c the duplicate is at the end
