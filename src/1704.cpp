#include <iostream>

using namespace std;

class Solution {
public:
    bool halvesAreAlike(string s) {
        int mid = s.size() / 2;
        string left = s.substr(0, mid);
        string right = s.substr(mid, s.size());
        int vowels = 0;
        for(char c : left) {
            c = tolower(c);
            if(c=='a'|c=='e'|c=='i'|c=='o'|c=='u') {
                vowels += 1;
            }
        }
        for(char c : right) {
            c = tolower(c);
            if(c=='a'|c=='e'|c=='i'|c=='o'|c=='u') {
                vowels -= 1;
            }
        }
        return vowels == 0;
    }
};
