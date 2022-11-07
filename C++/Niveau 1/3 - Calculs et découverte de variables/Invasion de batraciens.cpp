#include <iostream>
#define repeat(nb) for (int _loop = 1, _max = (nb); _loop <= _max; _loop++)
using namespace std;

int main(){

    int crapauds = 1337;

    repeat(12){
        crapauds = crapauds * 2;
    }

    cout << crapauds <<endl;

}