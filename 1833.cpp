#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int count = 0;
        sort(costs.begin(), costs.end());
        for(int price : costs) {
            if(price <= coins) {
                count++;
                coins -= price;
            }
            else{
                break;
            }
        }
        return count;
    }
};
