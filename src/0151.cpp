#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        stack<string> st;
        string word = "";
        for(char c : s) {
            if(c == ' ') {
                if(word.size() > 0) {
                    st.push(word);
                    word = "";   
                }
            }else {
                word += c;
            }
        }
        if(word == "") {
            word += st.top();
            st.pop();
        }
        while(!st.empty()) {
            word += ' ';
            word += st.top();
            st.pop();
        }
        return word;
    }
};