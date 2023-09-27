#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        const int mod = 1000000000 + 7;
        arr.insert(arr.begin(), 0);
        vector<int> result(arr.size());
        stack<int> st;
        st.push(0);
        for(int i = 0; i < arr.size(); ++i) {
            while(arr[st.top()] > arr[i]) {
                st.pop();
            }
            int j = st.top();
            result[i] = result[j] + (i-j)*arr[i];
            st.push(i);
        }
        long long sum = 0;
        for(int k : result) {
            sum += k;
        }
        return sum % mod;
    }
};
