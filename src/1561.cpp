#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        int ret = 0;
        int left = piles.size() / 3;
        for (int i = left; i < piles.size(); i += 2) {
            ret += piles[i];
        }
        return ret;
    }
};
