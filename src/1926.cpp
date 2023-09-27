#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        queue<vector<int>> Q;
        Q.push({entrance[0], entrance[1], 0});
        maze[entrance[0]][entrance[1]] = '+';
        while(Q.size()) {
            vector<int> loc = Q.front();
            int xo = loc[0], yo = loc[1], steps = loc[2];
            Q.pop();
            if((xo == 0 | yo == 0 | xo == m-1 | yo == n-1) && 
               (xo != entrance[0] | yo != entrance[1])) {
                return steps;
            }
            for(vector<int> dir : directions) {
                int xn = dir[0], yn = dir[1];
                int x = xo + xn, y = yo + yn;
                if (0 <= x && x < m && 0 <= y && y < n && maze[x][y] == '.') {
                    maze[x][y] = '+';
                    Q.push({x, y, steps+1});
                }
            }                
        }
        return -1;
    }
};
