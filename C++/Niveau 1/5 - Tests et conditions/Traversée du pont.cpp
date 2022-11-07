#include <iostream>

using namespace std;

int main(){
    
    int valeurDe1, valeurDe2;
    cin >> valeurDe1 >> valeurDe2;
    int sommeDes = valeurDe1+ valeurDe2;

    if(sommeDes >= 10){
        cout << "Taxe spéciale !" << endl;
        cout << 36 << endl;
    }else{
        cout << "Taxe régulière" << endl;
        cout << 2*sommeDes << endl;
    }

}