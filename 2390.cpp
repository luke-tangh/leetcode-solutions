#include <iostream>

using namespace std;

class Solution {
public:
    string removeStars(string s) {
        string str = "";
        for(char c : s) {
            if(c == '*') {
                str.pop_back();
            }else {
                str += c;
            }
        }
        return str;
    }
};