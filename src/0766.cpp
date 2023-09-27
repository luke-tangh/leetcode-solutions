#include <vector>

using namespace std;

class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        if(row < 1 or col < 1) {
            return true;
        }
        // vertically
        for(int i = 0; i < row; ++i) {
            int block = matrix[i][0];
            int r = i+1, c = 1;
            while(r < row and c < col) {
                if(matrix[r][c] != block) {
                    return false;
                }
                r++;
                c++;
            }
        }
        // horizontally
        for(int i = 1; i < col; ++i) {
            int block = matrix[0][i];
            int r = 1, c = 1+i;
            while(r < row and c < col) {
                if(matrix[r][c] != block) {
                    return false;
                }
                r++;
                c++;
            }
        }
        return true;
    }
};