#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ret = 0, prev = nums[0];
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] != prev) {
                ret += n - i;
                prev = nums[i];
            }
        }
        return ret;
    }
};
