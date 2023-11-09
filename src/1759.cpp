#include <iostream>

using namespace std;

class Solution {
public:
    int countHomogenous(string s) {
        char prev = s[0];
        long long mod = 1e9 + 7;
        long long count = 1, ret = 0;
        for(int i = 1; i < s.size(); ++i) {
            if(s[i] == prev) {
                count++;
            }
            else {
                ret += (1 + count) * count / 2;
                prev = s[i];
                count = 1;
            }
        }
        return (ret + (1 + count) * count / 2) % mod;
    }
};
