#include <iostream>
using namespace std;

int main(){
    int nombreNotes; 
    double sommeNotes = 0;
    
    cin >> nombreNotes;

    for(int i = 0; i < nombreNotes; i++){
        double note;

        cin >> note;

        sommeNotes += note;

    }

    double moyenneNote = sommeNotes/nombreNotes;

    cout << moyenneNote << endl;

}