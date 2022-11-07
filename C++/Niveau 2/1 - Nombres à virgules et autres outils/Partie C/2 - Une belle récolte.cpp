#include <iostream>
using namespace std;

int main(){
    int nombrePersonnes, nombreFruits;

    cin >> nombrePersonnes >> nombreFruits;

    if(nombreFruits % nombrePersonnes == 0){
        cout << "oui" << endl;
    }else{
        cout << "non" << endl;
    }

}