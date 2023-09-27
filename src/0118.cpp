#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> tria;
        tria.push_back({1});
        for(int i = 0; i < numRows-1; ++i) {
            vector<int> layer;
            layer.push_back({1});
            for(int j = 0; j < tria[i].size()-1; ++j) {
                layer.push_back({tria[i][j]+tria[i][j+1]});
            }
            layer.push_back({1});
            tria.push_back(layer);
        }
        return tria;
    }
};