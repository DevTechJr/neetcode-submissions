class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int max_len = 0;
        int s_len = s.size();
        unordered_set<char> mySet;
        for(int right = 0; right < s_len; right++){
            while(mySet.contains(s[right])){
                mySet.erase(s[left]);
                left++;
            }
           
           mySet.insert(s[right]);
           max_len = max(max_len, (int)mySet.size());

            // return max of max_len
        }
        return max_len;
    }
};
