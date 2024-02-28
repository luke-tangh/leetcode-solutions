#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> pres;
        int longest = 0, ptr = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (pres.count(s[i]) == 0) {
                longest = max(longest, i-ptr+1);
            }
            else {
                if (pres[s[i]] < ptr) {
                    longest = max(longest, i-ptr+1);
                }
                else {
                    ptr = pres[s[i]] + 1;    
                }
            }
            pres[s[i]] = i;
        }
        return longest;
    }
};
