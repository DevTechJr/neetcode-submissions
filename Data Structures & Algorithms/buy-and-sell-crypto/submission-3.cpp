class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // have a left and right pointer 
        // if the value of right is less than max, make left = right and clear greatest.
        // if the value fo right is greater, keep the loop

        int best = 0;
        int least = prices[0];
        int len_ = prices.size();
        for(int right = 0; right < len_; right ++){
            
            if(prices[right] < least){
                least = prices[right];
            }

            best = max(best, prices[right] - least);
        }

        return best;
    }
};
