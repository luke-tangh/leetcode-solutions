#include <queue>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int src, int dest) {
        unordered_map<int, vector<int>> graph;
        for(vector<int> e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        vector<bool> visited(n, false);
        queue<int> Q;
        Q.push(src);
        visited[src] = true;

        while(!Q.empty()) {
            int cur = Q.front();
            Q.pop();
            if(cur == dest) {
                return true;
            }
            for(int &node : graph[cur]) {
                if(!visited[node]) {
                    visited[node] = true;
                    Q.push(node);
                }
            }
        }
        return false;
    }
};
