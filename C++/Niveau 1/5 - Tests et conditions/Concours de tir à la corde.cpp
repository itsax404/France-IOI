#include <iostream>

using namespace std;

int main(){
    int sommeEquipe1 = 0, sommeEquipe2 = 0, nombreParticipants;

    cin >> nombreParticipants;

    for(int i = 1; i <= nombreParticipants; i++){
        int joueurEquipe1, joueurEquipe2;
        cin >> joueurEquipe1 >> joueurEquipe2;

        sommeEquipe1 += joueurEquipe1;
        sommeEquipe2 += joueurEquipe2;
    }

    if(sommeEquipe1 > sommeEquipe2){
        cout << "L'équipe 1 a un avantage" << endl;
        cout << "Poids total pour l'équipe 1 :" << " ";
        cout << sommeEquipe1 << endl;
        cout << "Poids total pour l'équipe 2 :" << " ";
        cout << sommeEquipe2 << endl; 
    }else{
        cout << "L'équipe 2 a un avantage" << endl;
        cout << "Poids total pour l'équipe 1 :" << " ";
        cout << sommeEquipe1 << endl;
        cout << "Poids total pour l'équipe 2 :" << " ";
        cout << sommeEquipe2 << endl; 
    }
}