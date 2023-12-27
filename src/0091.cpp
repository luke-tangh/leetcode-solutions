#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') {
            return 0;
        }

        vector<int> dp (s.size() + 1, 0);
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i < s.size() + 1; ++i) {
            if (0 < s[i - 1] - '0') {
                dp[i] = dp[i - 1];
            }
            int num = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
            if (10 <= num && num <= 26) {
                dp[i] += dp[i - 2];
            }
            if (dp[i] == 0 && dp[i - 1] == 0) {
                break;
            }
        }
        return dp[s.size()];
    }
};
