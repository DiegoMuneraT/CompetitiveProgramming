#include <iostream>
#include <stdio.h>
using namespace std;

class Solution {
public:
bool isSafe(vector<string> &queens, int row, int col, int n)
{
    char symbol = 'Q';
    for(int i = 0; i < row; i++)  // check in column
    {
        if(queens[i][col] == symbol) return false;
    }
    
    int i = row - 1;
    int j = col - 1;
    while(i >= 0 && j >= 0)  // check diagonally \ upwards
    {
        if(queens[i][j] == symbol) return false;
        i--; j--;
    }
    
    i = row - 1;
    j = col + 1;
    while(i >= 0 && j < n)  // check diagonally / upwards
    {
        if(queens[i][j] == symbol) return false;
        i--; j++;
    }
    return true;
}

void solve(vector<vector<string>> &ans, vector<string> &board, int row, int n)
{
    if(row == n) 
    {
        ans.push_back(board);
        return;
    }
    for(int col = 0; col < n ; col++){
        if(isSafe(board, row, col, n)){
            board[row][col] = 'Q';
        solve(ans, board, row+1, n);
            board[row][col] = '.';
        }   
    }
}

vector<vector<string>> solveNQueens(int n) 
{
    vector<string> queens(n, string(n, '.'));
    // as we want multiple answers so created one more else queens is enough
    vector<vector<string> > ans; 
    
    solve(ans, queens, 0, n); 
    return ans;
}
};