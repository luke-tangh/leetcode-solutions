#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxpro = 0, curpro = 0;
        for(int i = 1; i < prices.size(); ++i) {
            curpro = max(0, curpro + (prices[i]-prices[i-1]));
            maxpro = max(maxpro, curpro);
        }
        return maxpro;
    }
};
