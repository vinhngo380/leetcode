class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Utilize Array as your "LL"
        slow, fast = 0, 0
        while True: # First loop to identify 1st intersection....
            slow = nums[slow] 
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while True: # Second loop to identify 2nd intersection...
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return fast


'''
TLDR: Could NOT figure this out... without NeetCode. Damn. Utilizes Floyd Cycle Dectection
to find the first and second intersections. The first finds any intersection, the second finds the BEGINNING of the cycle.
Once these two match, then that is the result. Notice that we can use any element in the array as our index due to the constraints.

Super unintuitive, rec. the video.

TC O(n)
SC O(1)
'''
