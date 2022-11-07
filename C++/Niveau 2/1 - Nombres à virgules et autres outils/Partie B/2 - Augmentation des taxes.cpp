#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double taxeActuelle, nouvelleTaxe, prixActuel;

    cin >> taxeActuelle >> nouvelleTaxe >> prixActuel;

    double prixHorsTaxe = prixActuel/ ( 1 + (taxeActuelle/100));

    double futurPrix = prixHorsTaxe * (1 + (nouvelleTaxe/100));

    cout << round(futurPrix*100)/100 << endl;
}