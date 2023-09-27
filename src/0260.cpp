#include <vector>

using namespace std;

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long diff = 0;
        for(int n : nums) {
            diff ^= n;
        }
        diff &= -diff;
        vector<int> ret = {0, 0};
        for(int n : nums) {
            if(n & diff) {
                ret[0] ^= n;
            }else {
                ret[1] ^= n;
            }
        }
        return ret;
    }
};
