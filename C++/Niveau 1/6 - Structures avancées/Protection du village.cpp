#include <iostream>
using namespace std;

int main(){
    int nombreMaisons, xMin = 1000000, xMax = 0, yMin = 100000, yMax = 0;

    cin >> nombreMaisons;

    for(int i = 1; i <= nombreMaisons; i++){
        int xMaison, yMaison;
        cin >> xMaison >> yMaison;

        if(xMaison < xMin){
            xMin = xMaison;
        }
        if(xMaison > xMax){
            xMax = xMaison;
        }
        if(yMaison < yMin){
            yMin = yMaison;
        }
        if(yMaison > yMax){
            yMax = yMaison;
        }

    }
    int hauteur = yMax - yMin, largeur = xMax - xMin;
    int perimetre = 2*(largeur + hauteur);

    cout << perimetre << endl;

}