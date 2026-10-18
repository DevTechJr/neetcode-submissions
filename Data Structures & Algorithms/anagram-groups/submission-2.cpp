class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string> > charMap;
        vector<vector<string>> results;
        for (string &word: strs){
            vector<int> freq(26);
            for (char &letter: word){
                // for each letter
                int letter_ind = letter - 'a';
                freq[letter_ind]++;
            }
            string key = "";
            for (int &num: freq){
                key += to_string(num)+"#";
            }
            
            charMap[key].push_back(word);
        }

        for (auto& pair: charMap){
            results.push_back(pair.second);
        }

        return results;
    }
};
