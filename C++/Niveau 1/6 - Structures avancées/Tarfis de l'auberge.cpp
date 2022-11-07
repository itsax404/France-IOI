#include <iostream>
using namespace std;

int main(){

    int age, poidsBagages;

    cin >> age >> poidsBagages;

    if(age == 60){
        cout << 0 << endl;
    }else if(age < 10){
        cout << 5 << endl;
    }else if (poidsBagages >= 20){
        cout << 40 << endl;
    }else{
        cout << 30 << endl;
    }

}