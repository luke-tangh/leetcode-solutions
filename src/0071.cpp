#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> V;
        stack<string> S;
        string token = "";
        for(char c : path) {
            if(c == '/') {
                if(!token.empty()) {
                    V.push_back(token);
                    token.clear();
                }
            }else {
                token += c;
            }
        }
        if(!token.empty()) {
            V.push_back(token);
            token.clear();
        }
        for(string t : V) {
            if(t == ".") {
                continue;
            }else if(t == ".."){
                if(!S.empty()) {
                    S.pop();
                }
            }else {
                S.push(t);
            }
        }
        string cpath = "";
        while(!S.empty()) {
            cpath = S.top() + '/' + cpath;
            S.pop();
        }
        if(!cpath.empty()) cpath.pop_back();
        return '/' + cpath;
    }
};

