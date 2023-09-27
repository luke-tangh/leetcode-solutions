// warning : TLE code

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        unordered_map<char, int> boardic;
        for(int i = 0; i < board.size(); ++i) {
            for(int j = 0; j < board[0].size(); ++j) {
                char c = board[i][j];
                if(boardic.count(c)) {
                    boardic[c] += 1;
                }else {
                    boardic[c] = 1;
                }
            }
        }

        unordered_map<char, int> wordic;
        for(char c : word) {
            if(wordic.count(c)) {
                wordic[c] += 1;
            }else {
                wordic[c] = 1;
            }
        }

        for(pair<char, int> kv : wordic) {
            if(not boardic.count(kv.first) || boardic[kv.first] < kv.second) {
                return false;
            }
        }

        for(int i = 0; i < board.size(); ++i) {
            for(int j = 0; j < board[0].size(); ++j) {
                if(board[i][j] == word[0]) {
                    if(dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int k) {
        if(i < 0 || j < 0 || i >= board.size() || j >= board[0].size()) {
            return false;
        }
        if(k >= word.size() || word[k] != board[i][j]) {
            return false;
        }

        if(k == word.size() - 1) {
            return true;
        }

        vector<vector<int>> directions {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for(vector<int> direct : directions) {
            char temp = board[i][j];
            board[i][j] = '.';
            if(dfs(board, word, i+direct[0], j+direct[1], k+1)) {
                return true;
            }
            board[i][j] = temp;
        }
        return false;
    }
};
