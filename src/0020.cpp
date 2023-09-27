#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(char c : s) {
            switch(c) {
                case '[' : st.push(c); break;
                case '{' : st.push(c); break;
                case '(' : st.push(c); break;
                default : 
                    if(st.empty()) return false;
                    switch (c) {
                    case ']':
                        if(st.top() == '[') {
                            st.pop();
                            break;
                        }else {
                            return false;
                        }
                    case '}':
                        if(st.top() == '{') {
                            st.pop();
                            break;
                        }else {
                            return false;
                        }
                    case ')':
                        if(st.top() == '(') {
                            st.pop();
                            break;
                        }else {
                            return false;
                        }
                    default:
                        break;
                    }
            }
        }
        return st.empty(); 
    }
};
