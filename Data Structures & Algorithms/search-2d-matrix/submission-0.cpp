class Solution {
private:
    bool binary_search(vector<int>&row, int &target){
        int l = 0;
        int r = row.size()-1;
        while(l<=r){
            int mid = (l+r)/2;
            if(row[mid] < target){
                l = mid+1;
            } else if (row[mid] > target){
                r = mid-1;
            } else {
                return true;
            }
        }
        return false;
    }
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int l = 0;
        int r = matrix.size()-1;

        while(l <= r){
            int mid = (l+r)/2;
            if (matrix[mid][0] <= target && matrix[mid].back() >= target){
                bool result = binary_search(matrix[mid], target);
                return result;
            } else if (matrix[mid].back()<target){
                l = mid+1;
            } else if (matrix[mid][0] > target){
                r = mid-1;
            }
        }
        return false;

    }
};
