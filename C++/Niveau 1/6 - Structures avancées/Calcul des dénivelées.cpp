#include <iostream>
using namespace std;

int main(){
    int nombreVariations, totalMontees = 0, totalDescentes = 0;

    cin >> nombreVariations;

    for(int i = 1; i <= nombreVariations; i++){
        int variation;
        cin >> variation;

        if(variation < 0){
            totalDescentes += -(variation);
        }else{
            totalMontees += variation;
        }

    }

    cout << totalMontees << endl;
    cout << totalDescentes << endl;

}