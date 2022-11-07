#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double vitesseSon = 340.29;

    double dureeBruit;

    cin >> dureeBruit;

    double distanceEnMetre = dureeBruit * vitesseSon;

    int distanceEnKilometres = round(distanceEnMetre/1000);

    cout << distanceEnKilometres << endl;
}