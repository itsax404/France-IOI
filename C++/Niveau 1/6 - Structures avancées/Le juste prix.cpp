#include <iostream>
using namespace std;

int main(){

    int nombreMarchands, prixMarchandMin = 10000*10000, indexMarchand = 0;

    cin >> nombreMarchands;

    for(int i = 1; i <= nombreMarchands; i++){
        int prixMarchand;
        cin >> prixMarchand;

        if(prixMarchand < prixMarchandMin){
            prixMarchandMin = prixMarchand;
            indexMarchand = i;
        }else if(prixMarchand == prixMarchandMin){
            indexMarchand = i;
        }

    }

    cout << indexMarchand << endl;

}