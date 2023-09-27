#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        vector<vector<int>> count(26, vector<int>(26, 0));
        int ans = 0;
        for(string w : words) {
            int a = w[0] - 'a', b = w[1] - 'a';
            if(count[b][a]) {
                ans += 4;
                count[b][a]--;
            }else {
                count[a][b]++;
            }
        }
        for(int i = 0; i < 26; ++i) {
            if(count[i][i]) {
                ans += 2;
                break;
            }
        }
        return ans;
    }
};