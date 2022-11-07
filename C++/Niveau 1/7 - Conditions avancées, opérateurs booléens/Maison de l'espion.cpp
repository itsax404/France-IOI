#include <iostream>
using namespace std;

int main(){
    int maisonsSuspectes = 0,nombreMaisons, xMin, xMax, yMin, yMax;

    cin >> xMin >> xMax >> yMin >> yMax >> nombreMaisons;

    for(int i = 1; i <= nombreMaisons; i++){

        int x,y;

        cin >> x >> y;

        if(((xMin <= x) && (xMax >= x)) && ((yMin <= y) && (yMax >= y))){
            maisonsSuspectes++;
        }
    }

    cout << maisonsSuspectes << endl;

}