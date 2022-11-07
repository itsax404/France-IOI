#include <iostream>
using namespace std;

int main(){
    int nombrePierresMaximum, hauteur = 0, nombrePierresNecessaire = 0;

    cin >> nombrePierresMaximum;

    while((nombrePierresNecessaire) + ((hauteur+1)* (hauteur +1)) <= nombrePierresMaximum){
        hauteur++;
        nombrePierresNecessaire += (hauteur * hauteur);
    }

    cout << hauteur << endl;
    cout << nombrePierresNecessaire << endl;

}