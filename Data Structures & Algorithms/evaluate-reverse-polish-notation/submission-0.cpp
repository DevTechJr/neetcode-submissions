class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> operands;

        for (const std::string& token : tokens) {
            // Check if the token is an operator
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int right = operands.top();
                operands.pop();
                int left = operands.top();
                operands.pop();

                if (token == "+") {
                    operands.push(left + right);
                } else if (token == "-") {
                    operands.push(left - right);
                } else if (token == "*") {
                    operands.push(left * right);
                } else {
                    operands.push(left / right);
                }
            } else {
                // If it's a number, convert string to int using std::stoi
                operands.push(std::stoi(token));
            }
        }

        return operands.top();
    }
};