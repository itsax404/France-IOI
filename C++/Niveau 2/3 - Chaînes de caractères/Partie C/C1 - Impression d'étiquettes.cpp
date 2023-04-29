#include <iostream>
#include <string>

int main()
{
    std::string ligne;
    std::getline(std::cin, ligne);
    for(int i = 0; i < (int) ligne.length(); i++){
        std::cout << ligne[i] << std::endl;
    }
}