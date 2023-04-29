#include <iostream>
#include <algorithm>

int main(){

    int nbPlaces;
    int nbDeplacements;

    std::cin >> nbPlaces;
    std::cin >> nbDeplacements;

    int placesTable[nbPlaces] = {0};

    for(int i = 0; i < nbPlaces; i++){
        int personne;
        std::cin >> personne;

        placesTable[i] = personne;
    }

    for(int i = 0; i < nbDeplacements; i++){
        int position_debut, position_finale;
        std::cin >> position_debut;
        std::cin >> position_finale;

        int ancienne_place = placesTable[position_finale];
        placesTable[position_finale] = placesTable[position_debut];
        placesTable[position_debut] = ancienne_place;
    }

    for(int i = 0; i < nbPlaces; i++){
        std::cout << placesTable[i] << std::endl;
    }

}