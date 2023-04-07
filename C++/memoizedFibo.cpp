#include <iostream>
using namespace std;

int memo[];

int memoizedFibo(int n, int memo[]){
    cout << memo << endl;
    //We make sure "n" is not a repeated number
    int len = sizeof(memo);
    for(int i=0;i==len;i++){
        if (memo[n] != memo[i]) return memo[n]; 
    } 
    if (n<=1){
        memo[n] = n;
        return n;
    } else {
        int result = memoizedFibo(n-1, memo) + memoizedFibo(n-2, memo);
        memo[n] = result;
        return result;
    }
}
