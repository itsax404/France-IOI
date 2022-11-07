#include <iostream>
using namespace std;

int main(){

    int dateDebutSoldat1, dateFinSoldat1, dateDebutSoldat2,dateFinSoldat2;
    cin >> dateDebutSoldat1 >> dateFinSoldat1 >> dateDebutSoldat2 >>dateFinSoldat2; 


    if((dateFinSoldat2 < dateDebutSoldat1 )||(dateFinSoldat1 < dateDebutSoldat2)){
        cout << "Pas amis" << endl;
    }else{
        cout << "Amis" << endl;
    }
}