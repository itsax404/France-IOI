#include <iostream>
#include <string>

int main()
{
    int nbLignes;
    std::cin >> nbLignes;
    std::cin.ignore();
    for(int i = 0; i < nbLignes; i++){
        std::string ligne;
        std::getline(std::cin, ligne);
        for(int i = (int) ligne.length() - 1; i >= 0; i--){
            std::cout << ligne[i];
        }
        std::cout << std::endl;
    }
}