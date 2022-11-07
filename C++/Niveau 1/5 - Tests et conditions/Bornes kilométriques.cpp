#include <iostream>
using namespace std;

int main(){

    int borneKilometrique1, borneKilometrique2;
    cin >> borneKilometrique1 >> borneKilometrique2;

    int difference = borneKilometrique1-borneKilometrique2;

    if(difference < 0){
        cout << -difference <<endl;
    }else{
        cout << difference << endl;
    }
}