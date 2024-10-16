class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        # already sorted
        nums.sort()
        res = 0
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # find all unique three sums...
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            l, r = x+1, len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r] + nums[x]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    if nums[x] == nums[l] == nums[r]: # all same
                        res += (freq[nums[x]]) * (freq[nums[x]]-1) * (freq[nums[x]]-2) // 6
                    elif nums[x] == nums[l] != nums[r]: # First Two same
                        res += freq[nums[x]] * (freq[nums[l]]-1) * freq[nums[r]] // 2
                    elif nums[x] != nums[l] == nums[r]: # Last Two Same
                        res += freq[nums[x]] * freq[nums[l]] * (freq[nums[r]]-1) // 2
                    # we don't check for the if first and last are the same because that is impossible by our conditionals nums[x] == nums[x-1] and nums[l] == nums[l-1]
                    else: # all not same
                        res += freq[nums[x]] * freq[nums[l]] * freq[nums[r]]
                        
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res % (10**9 + 7)

  '''
  TLDR: Essentially three sum with a tricky modification. Look above for the modifications (in the if conditions) + their respective equations.

  TC O(n^2)
  SC O(n)
  '''
