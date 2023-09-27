#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temps) {
        stack<int> st;
        vector<int> ret(temps.size());
        for(int i = 0; i < temps.size(); ++i) {
            while(!st.empty() && temps[i] > temps[st.top()]) {
                int idx = st.top();
                st.pop();
                ret[idx] = i - idx;
            }
            st.push(i);
        }
        return ret;
    }
};
