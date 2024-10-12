class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return nums[i];
            }
        }
        return -1;
    }
}

/*

TLDR: Use the arrays sort to sort the numbers, then use the index n - 1 to check for duplicate and return the value

TC: O(n)
SC: O(logn) since i am using Sort which is a version of quicksort
*/
