#include <iostream>
#include <string>

int main()
{
    std::string auteur1, auteur2;
    getline(std::cin, auteur1);
    getline(std::cin, auteur2);

    if(auteur1 != auteur2){
        if(auteur1 < auteur2){
            std::cout << auteur1;
        }else{
            std::cout << auteur2;
        }
    }
}