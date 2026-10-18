class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for(string word: strs){
            result += to_string(word.size()) + "#"+ word;
        }
        return result;
    }

    vector<string> decode(string s) {
    vector<string> res;
    int i = 0;
    
    while (i < s.size()) {
        // Step 1: Find where the '#' is (starting from our current index `i`)
        int j = i;
        while (s[j] != '#') {
            j++;
        }
        
        // Step 2: Extract the length substring and convert it to an integer
        int length = stoi(s.substr(i, j - i));
        
        // Step 3: Move `j` past the '#' to the start of the actual word
        j++; 
        
        // Step 4: Extract the word using the length
        string word = s.substr(j, length);
        res.push_back(word);
        
        // Step 5: Advance our main pointer `i` past this word for the next iteration
        i = j + length;
    }
    
    return res;
}
};
