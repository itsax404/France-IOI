#include <iostream>

using namespace std;

int main(){

    int largeurSolMax;
    int largeurSolMin;
    cin >> largeurSolMax;
    cin >> largeurSolMin;

    int somme = 0;

    for(int i = largeurSolMax; i >= largeurSolMin; i--){
        somme += i*i;
    }

    cout << somme <<endl;

}