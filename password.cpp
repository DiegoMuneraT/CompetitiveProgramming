#include <bits/stdc++.h>
#include <iterator>
using namespace std;
#define vsc vector<set<char>>
#define vvc vector<vector<char>>
// 6x5 grid
// Each column: 26 UPPER
// Pass Length = 5
 
void fillGrid(vsc &grid){
    string gridRow;
    for(int i = 0; i < 6; ++i){
        cin >> gridRow;
        for(int j = 0; j < gridRow.size(); ++j){
            grid[j].insert(gridRow[j]);
        }
    }
}
 
bool solver(vvc &grid, int column, string solution, int &kAnswer){
    if(column == 5){
        if (kAnswer == 1){
            cout << solution;
            return true;
        }
        else{
            kAnswer--;
            return false;
        }
    }
    
    char selected;
    for(int i=0; i < grid[column].size(); ++i){
        selected = grid[column][i];
 
        if (solver(grid, column + 1, solution + selected, kAnswer)){
            return true;
        }
    }
 
    return false;
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);  
 
    int testCases, kthPassword;
    cin >> testCases;
 
    while(testCases--){
        vsc firstGrid(5, set<char>()), secondGrid(5, set<char>());
 
        cin >> kthPassword;
 
        fillGrid(firstGrid);
        fillGrid(secondGrid);
 
        vvc commonCharacters;
 
        int totalPossibilities = 1;
        for(int i = 0; i < 5; ++i){
            vector<char> common_char_col;
            set_intersection(firstGrid[i].begin(),firstGrid[i].end(),secondGrid[i].begin(),secondGrid[i].end(), std::back_inserter(common_char_col));
            commonCharacters.push_back(common_char_col);
 
            if (!common_char_col.size()){
                totalPossibilities = 0;
                break;
            }
            else {
                totalPossibilities *= common_char_col.size();
            }
        }
        
        if (!totalPossibilities || totalPossibilities < kthPassword){
            
            cout << "NO";
        }
        else{
            solver(commonCharacters, 0, "", kthPassword);
            if (kthPassword > 1){
                cout << "NO";
            }
        }
        cout << '\n';
    }
}