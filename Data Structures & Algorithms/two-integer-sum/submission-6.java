class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> past = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int check = target - nums[i];
            if(past.containsKey(check)){
                if(i <= past.get(check)) return new int[]{i, past.get(check)};
                return new int[]{past.get(check), i};
            }
            past.put(nums[i],i);
        }

        return new int[] {0,0};
    }
}
