#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int maxPair = 0;
        int i = 0, j = nums.size() - 1;
        while (i < j) {
            maxPair = max(nums[i] + nums[j], maxPair);
            i++;
            j--;
        }
        return maxPair;
    }
};
