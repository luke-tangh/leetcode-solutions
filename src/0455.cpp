#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int pg = 0, ps = 0;
        while (ps < s.size() && pg < g.size()) {
            if (g[pg] <= s[ps]) {
                pg++;
            }
            ps++;
        }
        return pg;
    }
};
