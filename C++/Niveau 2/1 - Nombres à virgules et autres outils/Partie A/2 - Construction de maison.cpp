#include <iostream>
#include <cmath>
using namespace std;

int main(){

    int prixCiment = 45;
    int poids1SacCiment = 60;

    double quantiteCiment;

    cin >> quantiteCiment;
    
    int quantiteCimentEntier = ceil(quantiteCiment/poids1SacCiment);

    int coutTotal = quantiteCimentEntier * prixCiment;

    cout << coutTotal << endl;

}