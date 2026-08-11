class Solution {
    public boolean canJump(int[] nums) {
        int i = nums.length - 2;
        int goal = nums.length - 1;
        while (i >= 0) {
            int curr = i + nums[i];
            if (curr >= goal) {
                goal = i;
            }
            i --;
        }
        return goal == 0;
    }
}
