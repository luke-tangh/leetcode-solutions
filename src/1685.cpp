#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int> ret;
        int left = 0;
        int right = accumulate(nums.begin(), nums.end(), 0);
        for (int i = 0; i < nums.size(); ++i) {
            ret.push_back(i * nums[i] - left + right - (nums.size() - i) * nums[i]);
            left += nums[i];
            right -= nums[i];
        }
        return ret;
    }
};
