#include <iostream>
using namespace std;

int main(){

    int hauteurArbre, nombreFolioles;
    cin >> hauteurArbre >> nombreFolioles;

    if(nombreFolioles >= 8){

        if(hauteurArbre <= 5){
            cout << "Tinuviel" << endl;
        }else{
            cout << "Calaelen" << endl;
        }

    }else{

        if(hauteurArbre >= 12){
            cout << "Dorthonion" << endl;
        }else{
            cout << "Falarion" << endl;
        }

    }

}