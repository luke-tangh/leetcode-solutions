#include <cmath>

class Solution {
public:
    int pivotInteger(int n) {
        int ans = (n * n + n) / 2;
        int sq = sqrt(ans);
        return sq * sq == ans ? sq : -1;
    }
};
