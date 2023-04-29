#include <iostream>
#include <string>

int main()
{
    int nombreLivre;
    std::cin >> nombreLivre;

    int longueurLivre = 0;

    std::cin.ignore();

    for(int i = 0; i < nombreLivre; i++)
    {
        std::string titre;
        std::getline(std::cin, titre);
        if(longueurLivre < (int) titre.length()){
            longueurLivre = titre.length();
            std::cout << titre << std::endl;
        }
    }

}