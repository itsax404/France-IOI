#include <iostream>
#include "robot.h"
using namespace std;

int main(){
 
    for(int a = 0; a<108; a++){
        for(int b =0; b<13; b++){
            haut();
        }
        for(int b =0; b<13; b++){
            droite();
        }
        for(int b =0; b<13; b++){
            bas();
        }
        for(int b =0; b<13; b++){
            gauche();
        }
    }

}