#include <iostream>
using namespace std;

int main(){

    int chiffre = 0, somme = 0;

    while(true){
        cin >> chiffre;
        if(chiffre == -1){
            break;
        }
        somme += chiffre;
    }

    cout << somme << endl;

}