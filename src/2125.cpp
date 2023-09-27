#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int ans = 0, prev = 0;
        for(int i = 0; i < bank.size(); ++i) {
            int num = count(bank[i].begin(), bank[i].end(), '1');
            if(num == 0){
                continue;
            }else{
                ans += prev*num;
                prev = num;
            }
        }
        return ans;
    }
};