#include <iostream>

using namespace std;

int main(){

    int nombreKarvas;
    cin >> nombreKarvas;

    for(int i = 1; i <= nombreKarvas; i++){
        int poids, age, longueur, hauteur;
        cin >> poids >> age >> longueur >> hauteur;

        int note = longueur*hauteur + poids;

        cout << note << endl; 
    }

}