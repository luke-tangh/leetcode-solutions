#include <vector>

using namespace std;

class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int dsum = 0;
        int maxlen = mat.size();
        for(int i = 0; i < maxlen; ++i) {
            dsum += mat[i][i];
            dsum += mat[maxlen-1-i][i];
        }
        if(maxlen % 2 != 0) {
            dsum -= mat[maxlen/2][maxlen/2];
        }
        return dsum;
    }
};