#include <iostream>
using namespace std;

int main(){

    int nombreCharrettes = 0;

    cin >> nombreCharrettes;

    double charrettes[nombreCharrettes] = {0};

    double sommeCharettes = 0;

    for(int i = 0; i < nombreCharrettes; i++){
        double poidsCharrette;
        cin >> poidsCharrette;

        charrettes[i] = poidsCharrette;

        sommeCharettes += poidsCharrette;
    }

    double poidsMoyen = sommeCharettes/nombreCharrettes;

    for(int i = 0; i < nombreCharrettes; i++){
        cout << poidsMoyen - charrettes[i] << endl;
    }

} 