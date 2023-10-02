#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> S;
        int mid = - pow(10, 9);

        reverse(nums.begin(), nums.end());
        for(int n : nums){
            if(n < mid) {
                return true;
            }
            while(!S.empty() && S.top() < n) {
                mid = S.top();
                S.pop();
            }
            S.push(n);
        }
        return false;
    }
};
