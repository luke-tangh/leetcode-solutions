#include <vector>
#include <queue>

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        queue<int> Q;
        Q.push(0);
        Q.push(0);
        Q.push(1);
        int mh = grid.size();
        int mw = grid[0].size();
        int shortest = INT_MAX;
        while (!Q.empty()) {
            int x = Q.front(); Q.pop();
            int y = Q.front(); Q.pop();
            int s = Q.front(); Q.pop();
            if (grid[y][x] != 0) continue;
            if (x + 1 == mw && y + 1 == mh) {
                shortest = min(shortest, s);
            }
            grid[y][x] = 1;
            if (x - 1 > -1) {
                Q.push(x - 1);
                Q.push(y);
                Q.push(s + 1);
            };
            if (x + 1 < mw) {
                Q.push(x + 1);
                Q.push(y);
                Q.push(s + 1);
            };
            if (y - 1 > -1) {
                Q.push(x);
                Q.push(y - 1);
                Q.push(s + 1);
            }
            if (y + 1 < mh) {
                Q.push(x);
                Q.push(y + 1);
                Q.push(s + 1);                
            }
            if (x - 1 > -1 && y - 1 > -1) {
                Q.push(x - 1);
                Q.push(y - 1);
                Q.push(s + 1);                
            }
            if (x + 1 < mw && y - 1 > -1) {
                Q.push(x + 1);
                Q.push(y - 1);
                Q.push(s + 1);                
            }
            if (x + 1 < mw && y + 1 < mh) {
                Q.push(x + 1);
                Q.push(y + 1);
                Q.push(s + 1);                
            }
            if (x - 1 > -1 && y + 1 < mh) {
                Q.push(x - 1);
                Q.push(y + 1);
                Q.push(s + 1);                
            }
        }
        return shortest == INT_MAX ? -1 : shortest;
    }
};
