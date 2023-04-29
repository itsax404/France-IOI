#include <iostream>
#include <string>

int main()
{
    int nombreLignes;
    std::cin >> nombreLignes;
    std::cin.ignore();
    for(int i = 0; i < nombreLignes; i++)
    {
        std::string ligne;
        getline(std::cin, ligne);
        if(i % 2 == 0){
            std::cout << ligne << std::endl;
        }
    }
}