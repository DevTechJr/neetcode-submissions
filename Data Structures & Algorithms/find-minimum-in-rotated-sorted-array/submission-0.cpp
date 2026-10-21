class Solution {
public:
    int findMin(vector<int> &nums) {
        int min = nums[0];

        for(int ind: nums){
            if (ind < min){
                min = ind;
            }
        }

        return min;
    }
};
