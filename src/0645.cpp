#include <numeric>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int sumA = accumulate(nums.begin(), nums.end(), 0);
        set<int> st(nums.begin(), nums.end());
        int sumB = accumulate(st.begin(), st.end(), 0);
        return {sumA - sumB, ((1 + n) * n / 2) - sumB};
    }
};
