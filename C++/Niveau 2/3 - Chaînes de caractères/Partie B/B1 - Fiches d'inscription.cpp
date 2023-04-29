#include <iostream>
#include <string>

int main()
{
    int nbPersonnes;
    std::cin >> nbPersonnes;

    for(int i = 0; i < nbPersonnes; i++)
    {
    std::string nom, prenom;
    std::cin >> prenom >> nom;
    std::cout << nom << " " << prenom << std::endl;
    }
}