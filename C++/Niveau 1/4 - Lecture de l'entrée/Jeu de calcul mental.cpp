#include <iostream>

using namespace std;

int main(){

    int nombreDepart = 66;
    int nombreRepetititons;
    cin >> nombreRepetititons;

    for(int i = 1; i <= nombreRepetititons; i++){
        nombreDepart *= i;
        cout << nombreDepart << endl;
    }

}