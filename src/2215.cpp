#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1(nums1.begin(), nums1.end());
        set<int> set2(nums2.begin(), nums2.end());
        for(auto n : nums2) {
            if(set1.count(n)) {
                set1.erase(n);
                set2.erase(n);
            }
        }
        vector<int> v1(set1.begin(), set1.end());
        vector<int> v2(set2.begin(), set2.end());
        return { v1, v2 };
    }
};
