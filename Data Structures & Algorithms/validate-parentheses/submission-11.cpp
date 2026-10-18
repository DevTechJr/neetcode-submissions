class Solution {
public:
    bool isValid(string s) {

unordered_map<char, char> string_map = {
            {'{', '}'},
            {'[', ']'},
            {'(', ')'}
        };
        
        vector<char> endings = {'}', ']', ')'};

        stack<char> myStack;

        for(char letter: s){
            if (string_map.count(letter)){
                myStack.push(letter);
            } else if (myStack.empty() && find(endings.begin(), endings.end(), letter) != endings.end()){
                return false;
            } else if (find(endings.begin(), endings.end(), letter) != endings.end()){
                char temp = myStack.top();
                myStack.pop();
                if (string_map[temp] != letter){
                    return false;
                }
            }

        }
        return myStack.empty();
    }
};


// stack<int> myStack;
// myStack.push(10);
// myStack.pop()
// myStack.top()
// check with myStack.empty() -> true if empty