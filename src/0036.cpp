#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<int> nums;
        for(int i = 0; i < 9; i++) {
            nums.clear();
            for(int j = 0; j < 9; ++j) {
                if(board[i][j] != '.') {
                    if(nums.count(board[i][j])) {
                        return false;
                    }else {
                        nums.insert(board[i][j]);
                    }
                }
            }
        }

        for(int i = 0; i < 9; i++) {
            nums.clear();
            for(int j = 0; j < 9; ++j) {
                if(board[j][i] != '.') {
                    if(nums.count(board[j][i])) {
                        return false;
                    }else {
                        nums.insert(board[j][i]);
                    }
                }
            }
        }

        for(int x = 0; x < 9; x += 3) {
            for(int y = 0; y < 9; y += 3) {
                nums.clear();
                for(int i = y; i < y + 3; i++) {
                    for(int j = x; j < x + 3; j++) {
                        if(board[i][j] != '.') {
                            if(nums.count(board[i][j])) {
                                return false;
                            }else {
                                nums.insert(board[i][j]);
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
};
