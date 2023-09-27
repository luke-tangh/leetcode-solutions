#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> map;
        for(string& s : strs) {
            string t = s;
            sort(t.begin(), t.end());
            map[t].push_back(s);
        }
        for(auto& e : map) {
            res.push_back(e.second);
        }
        return res;
    }
};