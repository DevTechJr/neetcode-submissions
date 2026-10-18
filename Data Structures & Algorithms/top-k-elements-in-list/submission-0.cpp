class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countMap;
        vector<int> finals;
        for(int num: nums){
            countMap[num]++;
        }
        vector<pair<int,int>> results(countMap.begin(), countMap.end());
        sort(results.begin(), results.end(), [](const auto& a, const auto& b){
            return a.second > b.second;
        });

        for(int ind = 0; ind<k;ind++){
            finals.push_back(results[ind].first);
        }
        return finals;
    }
};
