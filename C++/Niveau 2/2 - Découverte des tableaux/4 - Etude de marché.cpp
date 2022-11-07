#include <iostream>
using namespace std;

int main(){

    int nombreProduits = 10, nombrePersonnes;

    cin >> nombreProduits >> nombrePersonnes;

    int produits[nombreProduits]= {0};

    for(int i = 1; i<= nombrePersonnes; i++){
        int numeroProduit;
        
        cin >> numeroProduit;

        produits[numeroProduit] +=  1;

    }

    for(int i = 0; i < nombreProduits; i++){
        cout << produits[i] << endl;
    }



} 