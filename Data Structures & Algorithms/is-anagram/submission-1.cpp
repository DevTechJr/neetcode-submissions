class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (char letter: s){
            if(!s_map[letter]){
                s_map[letter] = 1;
            } else {
                s_map[letter] += 1;
            }
        };
                for (char letter: t){
            if(!t_map[letter]){
                t_map[letter] = 1;
            } else {
                t_map[letter] += 1;
            }
        };

        for (char letter: s){
            if (s_map[letter] != t_map[letter]){
                return false;
            }
        }

                for (char letter: t){
            if (s_map[letter] != t_map[letter]){
                return false;
            }
        }

        for (const auto& pair : s_map) {
    cout << pair.first << ": " << pair.second << "\n";}
    cout<<"new line"<<"\n";
    for (const auto& pair : s_map) {
    cout << pair.first << ": " << pair.second << "\n";
}


        return true;
    }
};
