#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        if(n < 1) {
            return ans;
        }
        string pare;
        backtrack(ans, pare, n, n);
        return ans;
    }
    
    void backtrack(vector<string> &ans, string &pare, int left, int right) {
        if(left > right || left < 0) {
            return;
        }
        if(left+right == 0) {
            ans.push_back(pare);
            return;
        }
        pare.push_back('(');
        backtrack(ans, pare, left-1, right);
        pare.pop_back();
        pare.push_back(')');
        backtrack(ans, pare, left, right-1);
        pare.pop_back();
    }
};
