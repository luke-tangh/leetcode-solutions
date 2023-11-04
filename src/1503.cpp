#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        if(left.empty()) {
            return n - *min_element(right.begin(), right.end());
        }
        else if(right.empty()) {
            return *max_element(left.begin(), left.end());
        }
        else {
            return max(*max_element(left.begin(), left.end()), 
            n - *min_element(right.begin(), right.end()));
        }
    }
};
