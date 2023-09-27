#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int count = 0;
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid[0].size(); ++j) {
                if(grid[i][j] == 0) {
                    count += dfs(grid, i, j);
                }
            }
        }
        return count;  
    }

    int dfs(vector<vector<int>>& grid, int x, int y) {
        queue<pair<int, int>> Q;
        Q.push(make_pair(x, y));
        bool boarder = false;
        while(!Q.empty()) {
            pair<int, int> axis = Q.front();
            int x = axis.first;
            int y = axis.second;
            Q.pop();
            if(grid[x][y] == 0) {
                grid[x][y] = 2;
                if(x + 1 < grid.size()) {
                    Q.push(make_pair(x + 1, y));
                }else {
                    boarder = true;
                }
                if(x - 1 > -1) {
                    Q.push(make_pair(x - 1, y));
                }else {
                    boarder = true;
                }
                if(y + 1 < grid[0].size()) {
                    Q.push(make_pair(x, y + 1));
                }else {
                    boarder = true;
                }
                if(y - 1 > -1) {
                    Q.push(make_pair(x, y - 1));
                }else {
                    boarder = true;
                }
            }
        }
        return boarder ? 0 : 1;
    }
};
