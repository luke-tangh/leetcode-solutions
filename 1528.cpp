#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string ans = s;
        for(int i = 0; i < indices.size(); ++i) {
            ans.replace(indices[i], 1, s.substr(i, 1));
        }
        return ans;
    }
};