#include <iostream>
using namespace std;

int main(){
    int heureArrivee;

    cin >> heureArrivee;

    int prix = 10;

    for(int i = 1; i <= heureArrivee; i++){
        prix += 5;
    }

    if(prix <= 53){
        cout << prix << endl;
    }else{
        cout << 53 << endl;
    }

}