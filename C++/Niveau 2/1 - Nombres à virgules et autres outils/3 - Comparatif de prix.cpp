#include <iostream>
using namespace std;

int main(){
    int nombreLegumes;
   
     cin >> nombreLegumes;
      
    for(int i = 0; i < nombreLegumes; i++){
        double masse, age, prix;
        cin >> masse >> age >> prix;

        double poids_au_kilo = prix/masse;

        cout << poids_au_kilo << endl;

    }

}