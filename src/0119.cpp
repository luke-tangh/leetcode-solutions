#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> tria;
        tria.push_back({1});
        for(int i = 0; i < rowIndex; ++i) {
            vector<int> layer;
            layer.push_back({1});
            for(int j = 0; j < tria[i].size()-1; ++j) {
                layer.push_back({tria[i][j]+tria[i][j+1]});
            }
            layer.push_back({1});
            tria.push_back(layer);
        }
        return tria[rowIndex];
    }
};
