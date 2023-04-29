#include <iostream>
#include <string>

int main()
{
    int nombreLivres, longueurMinimale;
    std::cin >> nombreLivres;
    std::cin >> longueurMinimale;
    std::cin.ignore();
    for(int i = 0; i < nombreLivres; i++)
    {
        std::string titre;
        std::string résumé;
        getline(std::cin, titre);
        getline(std::cin, résumé);
        
        if( (int) résumé.length() < longueurMinimale){
            std::cout << titre << std::endl;
        }
    }
}