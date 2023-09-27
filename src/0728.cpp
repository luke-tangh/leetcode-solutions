#include <vector>

using namespace std;

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for(left; left <= right; ++left) {
            if(selfDiv(left)) {
                ans.push_back(left);
            }
        }
        return ans;
    }
    
    bool selfDiv(int num) {
        int n = num;
        while(n) {
            int divs = n % 10;
            n /= 10;
            if(divs == 0) {
                return false;
            }
            if(num % divs != 0) {
                return false;
            }
        }
        return true;
    }
};