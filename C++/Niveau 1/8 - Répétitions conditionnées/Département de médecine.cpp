#include <iostream>
using namespace std;

int main(){
    
    int populationTotale;

    cin >> populationTotale;

    int populationTotaleContaminee = 1;
    int jour = 1;
    while(populationTotaleContaminee < populationTotale){
        populationTotaleContaminee = populationTotaleContaminee+ (populationTotaleContaminee * 2);
        jour++;
    }

    cout << jour << endl;

}