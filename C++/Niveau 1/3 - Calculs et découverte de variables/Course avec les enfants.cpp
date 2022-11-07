#include <iostream>
#include "robot.h"
using namespace std;

int main(){

    for(int x = 1; x <= 10; x++){
        for(int y = x; y <= 10; y++){
            droite();
        }
        ramasser();
        for(int y = x; y <= 10; y++){
            gauche();
        }
        deposer();
    }

}