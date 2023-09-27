#include <vector>

using namespace std;

class Solution {
public:
    int averageValue(vector<int>& nums) {
        int evens = 0, esum = 0;
        for(int n : nums) {
            if(n % 6 == 0) {
                esum += n;
                evens++;
            }
        }
        return evens == 0 ? 0 : esum / evens;
    }
};
