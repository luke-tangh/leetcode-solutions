#include <iostream>

using namespace std;

class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int longest = -1;
        for (char c = 'a'; c <= 'z'; c++) {
            int l = 0;
            int r = s.size() - 1;
            while (l < r) {
                if (s[l] == s[r] == c) {
                    longest = max(longest, r - l - 1);
                    break;
                }
                if (s[l] != c) l += 1;
                if (s[r] != c) r -= 1;
            }
        }
        return longest;
    }
};
