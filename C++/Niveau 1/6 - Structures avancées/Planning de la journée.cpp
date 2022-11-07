#include <iostream>
using namespace std;

int main(){
    int positionActuelle, nombreVillages, nombreVillagesAtteignables = 0;

    cin >> positionActuelle >> nombreVillages;

    for(int i = 1; i <= nombreVillages; i++){
        int distanceVillage;
        cin >> distanceVillage;
        int difference = 0;
        if(distanceVillage < positionActuelle){
            difference = positionActuelle - distanceVillage;
        }else{
            difference = distanceVillage - positionActuelle;
        }

        if(difference <= 50){
            nombreVillagesAtteignables++;
        }
    }

    cout << nombreVillagesAtteignables << endl;
}