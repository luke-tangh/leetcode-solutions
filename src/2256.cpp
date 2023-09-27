#include <vector>

using namespace std;

class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        long long lsum = 0, rsum = 0, temp = 0, minsum = LLONG_MAX;
        int size = nums.size(), maxloc = 0;
        if(nums.size() < 2) {
            return 0;
        }
        for(int i = 0; i < size; ++i) {
            rsum += nums[i];
        }
        for(int i = 0; i < size; ++i) {
            lsum += nums[i];
            rsum -= nums[i];
            if(i < size - 1) {
                temp = abs(lsum / (i+1) - rsum / (size-i-1) );
            }else {
                temp = abs(lsum / (i+1));
            }
            if(temp < minsum) {
                maxloc = i;
                minsum = temp;
            }
        }
        return maxloc;
    }
};
