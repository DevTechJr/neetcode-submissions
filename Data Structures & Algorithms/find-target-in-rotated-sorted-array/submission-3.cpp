class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int l = 0;
        int r= nums.size()-1;
        int mid;
        
        while(l <= r){
            mid = (l+r) /2;

            if(nums[mid] == target){return mid;}

            // check if left half is sorted
            if (nums[l] <= nums[mid]){
                // check if target is in left half
                if(nums[l] <= target && target < nums[mid]){
                    r = mid-1;
                } else {
                    l = mid+1;
                }

            } else {
                // right half is sorted
                if (nums[mid] < target && target <= nums[r]){
                    l = mid+1;
                } else {
                    r = mid-1;
                }
            } 



        }

        return -1;
    }
};
