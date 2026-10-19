class MinStack {
private:
    std::vector<int> main_stack;
    std::vector<int> min_stack;

public:
    MinStack() {
        // Constructor doesn't need to redeclare vectors
    }

    void push(int val) {
        main_stack.push_back(val);
        // Check if min_stack is empty first to avoid out-of-bounds access
        if (min_stack.empty() || val <= min_stack.back()) {
            min_stack.push_back(val);
        } else {
            min_stack.push_back(min_stack.back());
        }
    }
    
    void pop() {
        if (!main_stack.empty()) {
            main_stack.pop_back();
            min_stack.pop_back();
        }
    }
    
    int top() {
        if (!main_stack.empty()) {
            main_stack.back(); // Use .back() instead of [-1]
            return main_stack.back();
        }
        return -1;
    }
    
    int getMin() {
        if (!min_stack.empty()) {
            return min_stack.back();
        }
        return -1;
    }
};