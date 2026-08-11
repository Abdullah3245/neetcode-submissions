class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> num = new HashSet<>();

        for (int i = 0; i < nums.length; i ++) {
            if (num.contains(nums[i])) {
                 num.remove(nums[i]);
            } else {
                num.add(nums[i]);
            }
        }
        for (int i = 0; i < nums.length; i ++) {
            if (num.contains(nums[i])) {
                return nums[i];
            }
        }
        return 0;
    }
}
