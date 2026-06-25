// Last updated: 6/25/2026, 9:17:36 AM
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int start = 0, end = matrix.size()-1, m=matrix.size()-1, n=matrix[0].size()-1;
        for(int i=0; i<matrix.size()/2; i++){
            for(int j=start; j<end; j++){
                int temp = matrix[start][j];
                matrix[start][j] = matrix[m-j][n-end];
                matrix[m-j][n-end] = matrix[m-start][n-j];
                matrix[m-start][n-j] = matrix[j][end];
                matrix[j][end] = temp;
            }
            start++;
            end--;
        }
    }
};