#include <iostream>

using namespace std;

int main(int arr[]){
    int sol = sizeof(arr);
    for(int i = 0; i <= sizeof(arr); i++){
        sol += (i - arr[i]);
    }
    return sol;
}

/*
*/