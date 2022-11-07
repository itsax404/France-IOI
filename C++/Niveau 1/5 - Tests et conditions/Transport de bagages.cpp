#include <iostream>

using namespace std;

int main(){

    int nombrePaquets, poidsPaquets;
    cin >> nombrePaquets >> poidsPaquets;

    if((nombrePaquets * poidsPaquets) > 105){
        cout << "Surcharge !" << endl;
    }

}