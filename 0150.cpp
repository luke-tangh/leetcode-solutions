#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        long long temp = 0;
        for(int i = 0; i < tokens.size(); ++i) {
            if(tokens[i] == "+") {
                temp = st.top(); st.pop();
                temp += st.top(); st.pop();
                st.push(temp);
            }else if(tokens[i] == "-") {
                temp = st.top(); st.pop();
                temp = st.top() - temp; st.pop();
                st.push(temp);
            }else if(tokens[i] == "*") {
                temp = st.top(); st.pop();
                temp *= st.top(); st.pop();
                st.push(temp);
            }else if(tokens[i] == "/") {
                temp = st.top(); st.pop();
                temp = st.top() / temp; st.pop();
                st.push(temp);
            }else {
                st.push(atoi(tokens[i].c_str()));
            }
        }
        return st.top();
    }
};
