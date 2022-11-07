#include <iostream>
using namespace std;

int main(){
    int nombreJoursMarche, distanceMax = 0;

    cin >> nombreJoursMarche;

    for(int i = 1; i <= nombreJoursMarche; i++){
        int distance;
        cin >> distance;

        if(distance > distanceMax){
            distanceMax = distance;
        }

    }

    cout << distanceMax << endl;
}