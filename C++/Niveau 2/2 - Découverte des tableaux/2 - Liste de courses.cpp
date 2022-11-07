#include <iostream>
using namespace std;

int main(){
    int prixAuKilo[10] =  {9, 5, 12, 15, 7, 42, 13, 10, 1, 20};

    int somme = 0;

    for(int i = 0; i < 10 ; i++){
        int poids;
        cin >> poids;

        somme += (poids * prixAuKilo[i]);
    }

    cout << somme << endl;

} 