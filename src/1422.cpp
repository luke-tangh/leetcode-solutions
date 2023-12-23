#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int ret = 0;
        int l = 0;
        int r = count(s.begin(), s.end(), '1');
        s.pop_back();
        for (char c : s) {
            if (c == '1') {
                r -= 1;
            }
            else {
                l += 1;
            }
            ret = max(ret, l + r);
        }
        return ret;
    }
};
