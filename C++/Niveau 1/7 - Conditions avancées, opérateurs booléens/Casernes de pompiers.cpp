#include <iostream>
using namespace std;

int main(){
    int nombrePaires;

    cin >> nombrePaires;

    for(int i = 1; i <= nombrePaires; i++){
        int xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2;
        cin >> xMin1 >> xMax1 >> yMin1 >> yMax1 >> xMin2 >> xMax2 >> yMin2 >> yMax2;

        if((xMax2 <= xMin1) || (xMax1 <= xMin2) || (yMax2 <= yMin1) || (yMax1 <= yMin2)){
            cout << "NON" << endl;
        }else{
            cout << "OUI" << endl;
        }

    }

}