#include <iostream>
#include <algorithm>

int main(){

    int nbEmplacements;
    std::cin >> nbEmplacements;

    int positionMarchands[nbEmplacements] = {0};

    for(int i = 0; i < nbEmplacements; i++){
        int numeroMarchant;
        std::cin >> numeroMarchant;

        positionMarchands[numeroMarchant] = i;
    }

    for(int i = 0; i < nbEmplacements; i++){
        std::cout << positionMarchands[i] << std::endl;
    }


}