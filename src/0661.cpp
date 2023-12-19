#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        vector<vector<int>> dirs 
        = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 0}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        vector<vector<int>> smoothed(img.size(), vector<int>(img[0].size(), 0));
        for (int i = 0; i < img.size(); ++i) {
            for (int j = 0; j < img[0].size(); ++j) {
                int terms = 0;
                int value = 0;
                for (vector<int> dxy : dirs) {
                    int x = i + dxy[0];
                    int y = j + dxy[1];
                    if (x < 0 || x >= img.size())
                        continue;
                    if (y < 0 || y >= img[0].size())
                        continue;
                    terms += 1;
                    value += img[x][y];
                }
                smoothed[i][j] = floor(value / terms);
            }
        }
        return smoothed;
    }
};
