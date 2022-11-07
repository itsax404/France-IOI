#include <iostream>
using namespace std;

int main(){

    int dateDebut, dateFin, nombreEntrees,nombrePersonnesSuspectes = 0;

    cin >> dateDebut >> dateFin >>nombreEntrees;

    for(int i = 1; i <= nombreEntrees; i++){
        int jourArrivee;
        cin >> jourArrivee;

        if((dateDebut <= jourArrivee) && (dateFin >= jourArrivee)){
            nombrePersonnesSuspectes++;
        }
    }

    cout << nombrePersonnesSuspectes << endl;

}