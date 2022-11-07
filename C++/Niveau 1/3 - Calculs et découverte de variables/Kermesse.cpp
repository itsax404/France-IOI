#include <iostream>
using namespace std;

int main(){

    int bonbons = 0;

    for(int loop = 1; loop <= 50; loop++){
        bonbons += loop;
        cout << bonbons <<endl;
    }
}