class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // find max of entire pile
        int max_val = *max_element(piles.begin(), piles.end());
        

        // do binary search on this to find rate of k
        int l = 1;
        int r = max_val;
        int ans = max_val;
        while(l <= r){
            int k = (l+r) / 2;
            long long hours = 0;
            for (int num: piles){
                hours += (num+ k-1)/k;
            }
            if(hours <= h){
                ans = k;
                r = k-1;
            } else if (hours > h){
                l = k+1;
            } else {
                return ans;
            }
        }

        return ans;
        // once u have k, calculate hours it takes
        // if h is less than target, shift to lower
        // if h is higher than target, shift to higher bound
        
    }
};
