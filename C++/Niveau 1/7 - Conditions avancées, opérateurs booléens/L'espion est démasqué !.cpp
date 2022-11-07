#include <iostream>
using namespace std;

int main(){
    int nombrePersonnes;

    cin >> nombrePersonnes;

    for(int i = 1; i <= nombrePersonnes; i++){
        int taille, age, poids, cheval, cheveux;

        cin >> taille >> age >> poids >> cheval >> cheveux;

        int criteres = 0;

        if((taille >= 178) && (taille <= 182)){
            criteres++;
        }

        if(age >= 34){
            criteres++;
        }

        if(poids < 70){
            criteres++;
        }

        if(cheval == 0){
            criteres ++;
        }

        if(cheveux == 1){
            criteres++;
        }

        if(criteres == 0){
            cout << "Impossible" << endl;
        }else if(criteres == 5){
            cout << "Très probable" << endl;
        }else if((criteres >= 3) && (criteres <= 4)){
            cout << "Probable" << endl;
        }else{
            cout << "Peu probable" << endl;
        }

    }

}