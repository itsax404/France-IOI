#include <iostream>
using namespace std;

int main(){
    int dateDebut, dateFin, nombreInvites, suspects = 0;

    cin >> dateDebut >> dateFin >> nombreInvites;

    for(int i = 0; i < nombreInvites; i++){
        int dateDebutInvite, dateFinInvite;

        cin >> dateDebutInvite >> dateFinInvite;

        if(!((dateFinInvite < dateDebut) || (dateFin < dateDebutInvite))){
            suspects++;
        }

    }

    cout << suspects << endl;  

} 