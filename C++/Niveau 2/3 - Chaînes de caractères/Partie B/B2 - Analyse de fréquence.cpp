#include <iostream>
#include <string>

int main()
{
    int nbLignes, nbMots;
    std::cin >> nbLignes >> nbMots;

    int frequencesLongueurMots[101] = {0};

    for(int i = 0; i < nbLignes; i ++){
        for(int i = 0; i < nbMots; i++){
            std::string mot;
            std::cin >> mot;
            frequencesLongueurMots[(int) mot.length()]++;
        }
    }

    for(int i = 0; i < 101; i++){
        if(frequencesLongueurMots[i] != 0){
            std::cout << i << " : " << frequencesLongueurMots[i] << std::endl;
        }
    }
    
}