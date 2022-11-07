#include <iostream>
using namespace std;

int main(){

    int numeroMois;

    cin >> numeroMois;

    if(((1 <= numeroMois) && (numeroMois <= 3)) || ((7 <= numeroMois) &&(numeroMois <= 9))){
        cout << 30 << endl;
    }else if(numeroMois == 11){
        cout << 29 << endl;
    }else{
        cout << 31 << endl;
    }

}