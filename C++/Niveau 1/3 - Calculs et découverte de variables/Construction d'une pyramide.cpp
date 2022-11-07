#include <iostream>
using namespace std;

int main(){

    int cubes = 0;

    for(int x = 1; x <= 17; x+= 2){
        cubes += x*x*x;
    }

    cout << cubes << endl;

}