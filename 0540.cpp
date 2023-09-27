#include <vector>

using namespace std;

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = 0;
        for(int i : nums) {
            n ^= i;
        }
        return n;
    }
};
