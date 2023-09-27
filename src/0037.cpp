#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    char blank =  '.';

public:
    void solveSudoku(vector<vector<char>>& board) {
        backtrack(board, 0, 0);
    }

    bool backtrack(vector<vector<char>>& board, int r, int c) {
        while(board[r][c] != blank) {
            c++;
            if(c == 9) {
                c, r = 0, r+1;
            }
            if(r == 9) {
                return true;
            }
        }
        for(int k = 1; k < 10; ++k) {
            if(isValidMove(board, r, c, k+'0')) {
                board[r][c] = k + '0';
                if(backtrack(board, r, c)) {
                    return true;
                }
            }
        }
        board[r][c] = blank;
        return false;
    }

    bool isValidMove(vector<vector<char>>& board, int r, int c, char cand) {
        for(int i = 0; i < 9; ++i) {
            if(board[i][c] == cand) {
                return false;
            }
        }
        for(int j = 0; j < 9; ++j) {
            if(board[r][j] == cand) {
                return false;
            }
        }
        int br = 3*(r/3), bc = 3*(c/3);
        for(int i = br; i < br+3; ++i) {
            for(int j = bc; j < bc+3; ++j) {
                if(board[i][j] == cand) {
                    return false;
                }
            }
        }
        return true;
    }
};