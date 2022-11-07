#include <iostream>
using namespace std;

int main(){
    int nombreMesures, temperatureMin, temperatureMax;

    cin >> nombreMesures >> temperatureMin >> temperatureMax;

    int i = 0;

    while (i < nombreMesures){
        int temperature;

        cin >> temperature;

        if((temperature < temperatureMin) || (temperature > temperatureMax)){
            cout << "Alerte !!" << endl;
            break;
        }else{
            cout << "Rien à signaler" << endl;
        }

        i++;

    }

}