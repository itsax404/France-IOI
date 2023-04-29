#include <iostream>
#include <algorithm>

int main(){
    int nombreHabitants;
    std::cin >> nombreHabitants;
    int cadeaux[nombreHabitants] = {0};

    for (int i = 0; i < nombreHabitants; i++){
        int richesse;
        std::cin >> richesse;
        cadeaux[i] = richesse;
    }

    std::sort(cadeaux, cadeaux + nombreHabitants);

    if (nombreHabitants % 2 == 1){
        std::cout << cadeaux[(nombreHabitants-1)/2] << std::endl;
    }else{
        int valeur_inferieure = 0, valeur_superieure = 0;
        valeur_inferieure = cadeaux[nombreHabitants/2 - 1];
        valeur_superieure = cadeaux[nombreHabitants/2];
        std::cout << (valeur_inferieure + valeur_superieure)/2.0 << std::endl;
    }

}