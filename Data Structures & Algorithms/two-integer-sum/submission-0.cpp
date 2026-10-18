class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int num_len = nums.size();
        unordered_map<int, int> num_map;
        for(int ind =0; ind < num_len; ind++){
            int comp = target - nums[ind];

            if(num_map.contains(comp)){
                return {num_map[comp],ind };
            }

            num_map[nums[ind]] = ind;
        }
    }
};
