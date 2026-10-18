class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string,vector<string>> charMap;
        vector<vector<string>> results;

        for(string &word: strs){
            string key = word;
            sort(key.begin(), key.end());
            charMap[key].push_back(word);
        }

        for(const auto& pair: charMap){
            results.push_back(pair.second);
        }
        return results;
    }
};
