class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1): # loop to modify the cache
            for j in range(i+1, len(nums)): # checking indicies AFTER this current
                if nums[i] < nums[j]: # if the current number is less than the number at j index, we add 1 to the cache position of the current index.
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

  '''
  TLDR: USE DP. The Binary Search Solution is hard to come up with (though, it will be O(nlogn)).
  In essence, we are going backwards, checking the subsequent LIS cache to increase based on if nums[i] < nums[j], where i is the current number and nums[j] is every number after.
  The reason why we do max(LIS[i], 1+LIS[j]) is to compare the current LIS with whatever previous LIS we had stored in the cache. Of course, if there was one larger, we take that and add +1 (for the current)

  TC O(n^2) ... O(nlogn) is most optimal using binary search
  SC O(n)

  '''
