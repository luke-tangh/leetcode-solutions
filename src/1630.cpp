#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> ret;
        for (int i = 0; i < l.size(); ++i) {
            vector<int> subnum(nums.begin() + l[i], nums.begin() + r[i] + 1);
            ret.push_back(isArith(subnum));
        }
        return ret;
    }

    bool isArith(vector<int>& ns) {
        sort(ns.begin(), ns.end());
        int diff = ns[1] - ns[0];
        for(int i = 1; i < ns.size() - 1; ++i) {
            if (ns[i + 1] - ns[i] != diff) {
                return false;
            }
        }
        return true;
    }
};
