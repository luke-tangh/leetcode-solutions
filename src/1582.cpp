#include <vector>

using namespace std;

class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int ret = 0;
        vector<int> rows (mat.size(), 0);
        vector<int> cols (mat[0].size(), 0);
        for (int r = 0; r < mat.size(); ++r) {
            for (int c = 0; c < mat[0].size(); ++c) {
                if (mat[r][c] != 0) {
                    rows[r]++;
                }
            }
        }
        for (int c = 0; c < mat[0].size(); ++c) {
            for (int r = 0; r < mat.size(); ++r) {
                if (mat[r][c] != 0) {
                    cols[c]++;
                }
            }
        }
        for (int r = 0; r < mat.size(); ++r) {
            for (int c = 0; c < mat[0].size(); ++c) {
                if (mat[r][c] == 1 && rows[r] == 1 && cols[c] == 1) {
                    ret++;
                }
            }
        }
        return ret;
    }
};
