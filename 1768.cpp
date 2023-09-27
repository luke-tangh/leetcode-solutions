#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int bound = min(word1.size(), word2.size());
        string merged = "";
        for(int i = 0; i < bound; ++i) {
            merged += word1[i];
            merged += word2[i];
        }
        while(bound < word1.size()) {
            merged += word1[bound];
            bound++;
        }
        while(bound < word2.size()) {
            merged += word2[bound];
            bound++;
        }
        return merged;
    }
};
