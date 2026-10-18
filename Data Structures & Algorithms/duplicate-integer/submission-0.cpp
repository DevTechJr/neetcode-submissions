class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> myMap;
        int numsLen = nums.size();
        bool result = false;

        for (int ind = 0; ind < numsLen; ind++){
            if(myMap[nums[ind]]){
                return true;
            }

            myMap[nums[ind]] = true;
        }

        return result;
    }
};