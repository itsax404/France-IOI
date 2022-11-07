#include <iostream>

using namespace std;

int main(){

    int somme = 0;

    for(int i = 1; i <= 20; i++){
        int entree;
        cin >> entree;

        somme += entree;
    }

    cout << somme << endl;

}