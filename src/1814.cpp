#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        long long pairs = 0;
        unordered_map<int, int> count;
        for (int i = 0; i < nums.size(); ++i) {
            nums[i] -= rev(nums[i]);
            pairs += count[nums[i]];
            count[nums[i]] += 1;
        }
        return pairs % (int) (1e9 + 7);
    }

    int rev(int n) {
        int r = 0;
        while (n > 0) {
            r *= 10;
            r += n % 10;
            n /= 10;
        }
        return r;
    }
};
