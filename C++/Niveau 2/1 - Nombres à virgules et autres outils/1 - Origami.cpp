#include <iostream>
using namespace std;

int main(){
    double epaisseur = 0.0110;
    for (int i = 0; i < 15; i++){
        epaisseur *= 2;
    }

    cout << epaisseur << endl;
}