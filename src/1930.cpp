#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int ret = 0;
        set<char> S;
        for (char c = 'a'; c <= 'z'; ++c) {
            int lp = 0;
            int rp = s.size() - 1;
            S.clear();
            while (lp < rp && !(s[lp] == c && s[rp] == c)) {
                if (s[lp] != c) { lp++; }
                if (s[rp] != c) { rp--; }
            }
            if (s[lp] == c && s[rp] == c) {
                for (int i = lp + 1; i < rp; ++i) {
                    S.insert(s[i]);
                }
                ret += S.size();
            }
        }
        return ret;
    }
};
