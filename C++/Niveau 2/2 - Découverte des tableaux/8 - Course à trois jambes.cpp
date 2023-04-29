#include <iostream>
#include <algorithm>

int main(){

    int nbParticipants;
    std::cin >> nbParticipants;
    int nombreChoisiParticipants[nbParticipants] = {0};

    for(int i = 0; i < nbParticipants; i++){
        int nombreChoisi;
        std::cin >> nombreChoisi;
        nombreChoisiParticipants[i] = nombreChoisi;
    }

    std::sort(nombreChoisiParticipants, nombreChoisiParticipants + nbParticipants);

    for(int i = 0; i < nbParticipants/2; i++){
        std::cout << nombreChoisiParticipants[i] << " " << nombreChoisiParticipants[(nbParticipants-1) - i] << std::endl;
    }

}