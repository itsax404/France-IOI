#include <iostream>
using namespace std;

int main(){

    int nombreDeplacements = 0;

    cin >> nombreDeplacements;

    int deplacements[nombreDeplacements] = {0};

    for(int i = 0; i < nombreDeplacements; i++){
        int deplacement;
        cin >> deplacement;

        deplacements[i] = deplacement;

    }

    for(int i = nombreDeplacements-1; i >= 0; i--){
        int deplacementAFaire = 0;

        int deplacement = deplacements[i];

        if(deplacement == 1){
            deplacementAFaire = 2;
        }else if (deplacement == 2){
            deplacementAFaire = 1;
        }else if (deplacement == 3){
            deplacementAFaire = 3;
        }else if (deplacement == 4){
            deplacementAFaire = 5;
        }else{
            deplacementAFaire = 4;
        }
    
        
        cout << deplacementAFaire << endl;
    }

} 