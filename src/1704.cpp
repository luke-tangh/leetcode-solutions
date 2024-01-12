#include <iostream>

using namespace std;

class Solution {
public:
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    bool halvesAreAlike(string s) {
        int mid = s.size() / 2;
        string left = s.substr(0, mid);
        string right = s.substr(mid, s.size());
        int vowels = 0;
        for(int i = 0; i < left.size(); ++i) {
            if (isVowel(tolower(left[i]))) vowels++;
            if (isVowel(tolower(right[i]))) vowels--;
        }
        return vowels == 0;
    }
};
