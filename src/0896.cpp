#include <vector>

using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        return isDec(nums) || isAsc(nums);
    }

    bool isDec(vector<int> n) {
        for(int i = 0; i < n.size() - 1; ++i) {
            if(n[i] < n[i + 1]) {
                return false;
            }
        }
        return true;
    }
    
    bool isAsc(vector<int> n) {
        for(int i = 0; i < n.size() - 1; ++i) {
            if(n[i] > n[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
