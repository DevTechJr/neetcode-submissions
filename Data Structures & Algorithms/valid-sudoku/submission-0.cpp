class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> seen;

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char current = board[i][j];
                
                // Skip empty cells
                if (current == '.') continue;

                // Create unique string identifiers for row, column, and 3x3 box
                string row_key = string(1, current) + " in row " + to_string(i);
                string col_key = string(1, current) + " in col " + to_string(j);
                string box_key = string(1, current) + " in box " + to_string(i / 3) + "-" + to_string(j / 3);

                // If any of these already exist in our set, the board is invalid
                if (seen.count(row_key) || seen.count(col_key) || seen.count(box_key)) {
                    return false;
                }

                // Otherwise, record them as seen
                seen.insert(row_key);
                seen.insert(col_key);
                seen.insert(box_key);
            }
        }

        return true;
    }
};