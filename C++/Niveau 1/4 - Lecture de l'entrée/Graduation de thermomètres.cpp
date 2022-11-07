#include <iostream>

using namespace std;

int main(){

    int temperatureMin;
    int temperatureMax;
    cin >> temperatureMin;
    cin >> temperatureMax;

    for(int i = temperatureMin; i <= temperatureMax; i++){
        cout << i << endl;
    }

}