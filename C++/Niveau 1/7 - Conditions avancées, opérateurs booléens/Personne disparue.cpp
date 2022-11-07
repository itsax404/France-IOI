#include <iostream>
using namespace std;

int main(){

    int numeroPersonne, nombresEntrees;

    cin >> numeroPersonne >> nombresEntrees;

    bool estEncoreDansLaVille = true;

    for(int i = 1; i <= nombresEntrees; i++){
        int numero;

        cin >> numero;

        bool estPlusDansLaVille = (numero == numeroPersonne);

        if(estPlusDansLaVille){
            cout << "Sorti de la ville" << endl;
            estEncoreDansLaVille = false;
            break;
        }
    }
    
    if(estEncoreDansLaVille){
        cout << "Encore dans la ville" << endl;
    }
}