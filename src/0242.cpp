#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> ana;
        for (char c : s) {
            ana[c]++;
        }
        for (char c : t) {
            ana[c]--;
        }
        for (auto kv : ana) {
            if (kv.second != 0) {
                return false;
            }
        }
        return true;
    }
};
