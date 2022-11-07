#include <iostream>
using namespace std;

int main(){

    int nombreOperations;

    cin >> nombreOperations;

    int livres[10]= {0};

    for(int i = 1; i<= nombreOperations; i++){
        int numeroLivre, operation;

        cin >> numeroLivre >> operation;

        livres[numeroLivre-1] += operation;

    }

    for(int i = 0; i < 10; i++){
        cout << livres << endl;
    }



} 