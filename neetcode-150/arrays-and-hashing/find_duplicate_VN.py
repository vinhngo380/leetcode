class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #since we just need to store if there was > 1 instance
        #store the first instances in a cache, if it appears
        #then return True since that means there are more than
        #one of the nums
        #TC: O(n); searching in the cache takes O(1) and we must
        #go through the whole array at worst
        #SC: O(n); if there are no duplicates then we had to copy
        #the array in the hashset
        cache = set() 
        for num in nums:
           if num in cache:
               return True
           cache.add(num)
        return False
