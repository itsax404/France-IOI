#include <iostream>

using namespace std;

int main(){

    int positionDepart;
    int largeurEmplacement;
    int nombreVendeurs;
    cin >> positionDepart;
    cin >> largeurEmplacement;
    cin >> nombreVendeurs;
    cout << positionDepart << endl;
    for(int i = 1; i <= nombreVendeurs; i++){
        positionDepart += largeurEmplacement;
        cout << positionDepart << endl;
    }

}