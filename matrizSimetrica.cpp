#include<iostream>
#include<math.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main(){
    auto start = high_resolution_clock::now();

    int filas, columnas, simetrica = 0;

    cout << "Digite el numero de columnas: "; cin >> columnas;
    cout << "Digite el numero de filas: "; cin >> filas;

    int matriz[filas][columnas];

    // Llenamos la matriz
    if(filas == columnas){
        for(int i = 0; i < filas; i++){
            for(int j = 0; j < columnas; j++){
                cout << "Digite un numero ["<<i+1<<"]["<<j+1<<"]: ";
                cin >> matriz[i][j];
            }
        }
    }
    // Comparamos con su transpuesta
    for(int i = 0; i < filas; i++){
        for(int j = 0; j < columnas ; j++){
            if(matriz[i][j] != matriz[j][i]){
                simetrica +=1;
            }
        }
    }
    // Verificamos si es simetrica
    if((filas*columnas) == simetrica){
        cout << "\nLa matriz es simetrica" << endl;
    }else{
        cout << "\nLa matriz no es simetrica" << endl;
    }

    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);
    cout << "\nTime taken: " << duration.count() << "ms" << endl;
    
    return 0;
}