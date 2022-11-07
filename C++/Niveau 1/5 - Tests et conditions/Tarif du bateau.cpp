#include <iostream>
using namespace std;

int main(){

    int agePersonne;
    cin >> agePersonne;

    if(agePersonne < 21){
        cout << "Tarif réduit" << endl;
    }else{
        cout << "Tarif plein" << endl;
    }

}