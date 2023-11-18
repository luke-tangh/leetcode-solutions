#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long i = 0, j = 0;
        for (int n = 0; n < nums.size() - 1; ++n) {
            if (k < 0) {
                k = k + (nums[j] - nums[i]) - (j - i) * (nums[j + 1] - nums[j]);
                i++;
                j++;
            }
            else {
                j++;
                k -= (j - i) * (nums[j] - nums[j - 1]);
            }
        }
        return k < 0 ? j - i : j - i + 1;
    }
};
