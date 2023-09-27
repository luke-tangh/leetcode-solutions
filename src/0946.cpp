#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> S;
        int index = 0;
        for(int n : pushed) {
            S.push(n);
            while(!S.empty() && S.top() == popped[index]) {
                S.pop();
                index++;
            }
        }
        return S.empty();
    }
};
