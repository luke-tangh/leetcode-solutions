#include <iostream>

using namespace std;

class Solution {
public:
    int size = 0;
    string str = "";

    string longestPalindrome(string s) {
        size = s.size();
        str = s;
        string max_str = "";
        string l = "", r = "";
        for(int i = 0; i < size; ++i) {
            l = palindrome(i, i);
            r = palindrome(i, i+1);
            if(l.size() > max_str.size()) {
                max_str = l;
            }else if(r.size() > max_str.size()) {
                max_str = r;
            }
        }
        return max_str;

    }

    string palindrome(int left, int right) {
        while(left >= 0 && right < size && str[left] == str[right]) {
            left--;
            right++;
        }
        return str.substr(left+1, right-left);
    }
};
