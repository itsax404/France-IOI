#include <iostream>
using namespace std;

int main(){
    int code, codeSecret = 64741;

    cin >> code;

    if(code != codeSecret){
        cout << "Allez-vous en !";
    }else{
        cout << "Bon festin !";
    }
}