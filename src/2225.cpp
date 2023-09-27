#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> loses;
        vector<int> nol, onel;
        vector<vector<int>> ans;
        for(vector<int> mat : matches) {
            if(!loses.count(mat[0])) {
                loses[mat[0]] = 0;
            }
            if(!loses.count(mat[1])) {
                loses[mat[1]] = 1;
            }else {
                loses[mat[1]] += 1;
            }
        }
        for(auto [k, v] : loses) {
            if(v == 0) {
                nol.push_back(k);
            }else if(v == 1) {
                onel.push_back(k);
            }
        }
        ans.push_back(nol);
        ans.push_back(onel);
        return ans;
    }
};
