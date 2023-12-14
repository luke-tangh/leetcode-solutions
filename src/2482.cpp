#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid[0].size();
        int n = grid.size();
        vector<vector<int>> ret(n, vector<int>(m, 0));
        vector<int> rows (n, 0);
        vector<int> cols (m, 0);
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                if (grid[r][c] != 0) {
                    rows[r]++;
                }
            }
        }
        for (int c = 0; c < m; ++c) {
            for (int r = 0; r < n; ++r) {
                if (grid[r][c] != 0) {
                    cols[c]++;
                }
            }
        }
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                ret[r][c] = 2 * (rows[r] + cols[c]) - (n + m);
            }
        }
        return ret;
    }
};
