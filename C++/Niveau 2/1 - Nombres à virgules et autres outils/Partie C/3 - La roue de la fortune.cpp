#include <iostream>
using namespace std;

int main(){
    int nombreZones;

    cin >> nombreZones;
    if(nombreZones < 0){
        cout << nombreZones % 24 + 24 << endl;   
    }else{
        cout << nombreZones % 24 << endl;
    }

} 