#include <iostream>
using namespace std;

int main(){

    int nombreJeton;

    cin >> nombreJeton;

    for(int i = 1; i <= nombreJeton; i++){

        int x, y;

        cin >> x >> y;

        bool estDansLaFeuille = (((0 <= x) && (x <= 90)) && ((0 <= y) && (y <= 70)));

        bool estDaneZone1Rouge = (((60 <= y) && (y <= 70)) && ((15 <= x) && (x <= 45)));
        bool estDaneZone2Rouge = (((60 <= y) && (y <= 70)) && ((60 <= x) && (x <= 85)));
        bool estDansZoneRouge = (estDaneZone1Rouge ||estDaneZone2Rouge);

        bool estDaneZone1Bleue = (((10 <= y) && (y <= 20)) && ((10 <= x) && (x <= 85)));
        bool estDaneZone2Bleue = (((20 <= y) && (y <= 45)) && ((10 <= x) && (x <= 25)));
        bool estDaneZone3Bleue = (((20 <= y) && (y <= 45)) && ((50 <= x) && (x <= 85)));
        bool estDaneZone4Bleue = (((45 <= y) && (y <= 55)) && ((10 <= x) && (x <= 85)));
        bool estDansZoneBleue = (estDaneZone1Bleue || estDaneZone2Bleue || estDaneZone3Bleue || estDaneZone4Bleue);

        if(!estDansLaFeuille){
            cout << "En dehors de la feuille" << endl;
        }else if(estDansZoneRouge){
            cout << "Dans une zone rouge" << endl;
        }else if(estDansZoneBleue){ 
            cout << "Dans une zone bleue" << endl;
        }else{
            cout << "Dans une zone jaune" << endl;
        }

    }


}   