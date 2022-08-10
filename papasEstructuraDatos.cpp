#include <iostream>
using namespace std;

//1. Fuerza bruta  // 2. Backtracking // 3. Divide and conquer // 4. Programación dinámica

//Algoritmo que define la solución del problema (Popes). Las variables que controlan la magnitud del problema
//son  (p,y). La complejidad en el peor de los casos del algoritmo es de O(Y * P)"""

//Loop recursivo
#define solve(i,n) for(int i=0; i<n;i++)

//lista de los papas 
int popes[100000];

int main(void){
    //variables de entrada
    int y, p;
    int count, start, end, best;

    //aquí se llena la lista de papas hasta que i llegue al tope de papas definido por "P"
    while(cin >> y >> p){
        solve (i, p){
            cin >> popes[i];
        }
        count = start = end = best = 0;

        //empezamos a recorrer la lista de los papas
        solve (i, p){
            count = 0;
            int j = i;
            //Mientras j sea menor al numero de papas y el papa en la posición [j] controlada por solve sea menor que el papa en la posición [i]+y
            //el arreglo se recorre de a 2 elementos y deja de tener en cuenta alguno que no cumpla la condición algo parecido a lo que haría una busqueda binaria
            while (j < p && popes[j] < popes[i] + y){
                //aumentamos j en 1 para controlar el while & evaluar el próximo papa, asi mismo aumentamos el conteo de papas
                j++;
                count++;
            }
            //swap entre count start, best, end & count 
            if (count > best){
                best = count;
                start = popes[i];
                end = popes[j-1];
            }
        }
        //imprimimos el resultado
        cout << best << " " << start << " " << end << endl;
    }
    return 0;
}