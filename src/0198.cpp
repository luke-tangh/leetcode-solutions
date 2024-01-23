#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int last = 0, now = 0;
        for (int i : nums) {
            int temp = now;
            now = max(last + i, now);
            last = temp;
        }
        return now;
    }
};
