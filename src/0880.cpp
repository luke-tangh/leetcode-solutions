#include <iostream>

using namespace std;

class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long length = 0;
        int index = 0;
        while(length < k) {
            if(isdigit(s[index])) {
                length *= (s[index]) - '0';
            }else {
                length++;
            }
            index++;
        }
        for(int j = index - 1; j >= 0; --j) {
            if(isdigit(s[j])) {
                length /= s[j] - '0';
                k %= length;
            }else {
                if(k == 0 || k == length) {
                    return string(1, s[j]);
                }
                length--;
            }
        }
        return "";
    }
};
