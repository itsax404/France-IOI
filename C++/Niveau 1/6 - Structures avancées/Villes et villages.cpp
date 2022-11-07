#include <iostream>
using namespace std;

int main(){
    int nombreVilles = 0, nombreLieux;

    cin >> nombreLieux;

    for(int i = 1; i <= nombreLieux; i++){
        int nombreHabitants;
        cin >> nombreHabitants;

        if(nombreHabitants > 10000){
            nombreVilles++;
        }

    }  

    cout << nombreVilles << endl;
}