#include <iostream>
using namespace std;

int main(){

    bool aTrouve = false;
    int chiffreATrouver, nombreTentative = 0;

    cin >> chiffreATrouver;

    while (!aTrouve){
        int proposition;
        cin >> proposition;

        if(proposition < chiffreATrouver){
            cout << "c'est plus" << endl;
            nombreTentative++;
        }else if(proposition > chiffreATrouver){
            cout << "c'est moins" << endl;
            nombreTentative++;
        }else{
            aTrouve = true;
            nombreTentative++;
        }

    }

    cout << "Nombre d'essais nécessaires :"<< endl;
    cout << nombreTentative << endl;

}