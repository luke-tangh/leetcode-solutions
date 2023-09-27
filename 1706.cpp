#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> res;
        for(int i = 0; i < n; ++i) {
            int i1 = i, i2;
            for(int j = 0; j < m; ++j) {
                i2 = i1 + grid[j][i1];
                if (i2 < 0 || i2 >= n || grid[j][i2] != grid[j][i1]) {
                    i1 = -1;
                    break;
                }
                i1 = i2;
            }
            res.push_back(i1);
        }
        return res;
    }
};

/*
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector result(grid.size(), 0);
        for(int i = 0; i < grid[0].size(); ++i) {
            int cur_row = 0, cur_col = i;
            while(cur_row < grid.size()) {
                if(grid[cur_row][cur_col] == 1 && cur_col+1 < grid[0].size() && grid[cur_row][cur_col+1] == 1) {
                    cur_col++;
                    cur_row++;
                }else if(grid[cur_row][cur_col] == -1 && cur_col-1 >= 0 && grid[cur_row][cur_col-1] == -1) {
                    cur_col--;
                    cur_row++;
                }else {
                    break;
                }
            }
            result[i] = cur_row == grid.size() ? cur_col : -1;
        }
        return result;
    }
};
*/