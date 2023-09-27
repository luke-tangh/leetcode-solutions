#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string decodeMessage(string key, string message) {
        int keyidx = 0;
        string ans = "";
        unordered_map<char, char> keymap;
        for(char k : key) {
            if(k == ' ') {
                continue;
            }
            if(keymap.count(k) != 0) {
                continue;
            }
            keymap[k] = 'a' + keyidx++;
        }
        for(char k : message) {
            if(k != ' ') {
                k = keymap[k];
            }
            ans += k;
        }
        return ans;
    }
};