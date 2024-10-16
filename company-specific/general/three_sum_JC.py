class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)):
            if x > 0 and nums[x-1] == nums[x]:
                continue
            l, r = x+1, len(nums) - 1
            while l < r:
                curr = nums[x] + nums[l] + nums[r] 
                if curr > 0: 
                    r -= 1
                elif curr < 0: 
                    l += 1
                else:
                    res.append([nums[x],nums[l],nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

'''
TLDR: Basically two sum with an extra pointer. Fix one pointer (x) and have l, r to iterate through everything between x+1 and len(nums) -1.
We have some conditional checks to avoid duplicate, like check if nums[x-1] == nums[x] as well as the inner check nums[l] == nums[l-1].

TC O(n)
SC O(1)
'''
