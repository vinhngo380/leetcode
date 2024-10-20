class Solution:
    #start at each end, use the fact that the list is sorted so that you
    #can move the left pointer to the right increase val or move right pointer
    #to the left to decrease val
    #TC: O(n)
    #SC: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return [left + 1, right + 1]

