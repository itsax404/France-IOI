#include <iostream>
#include <string>

int main(){
    for(int i = 0; i < 6; i++) {
        std::string titre, auteur;
        std::getline(std::cin, auteur);
        std::getline(std::cin, titre);
        std::cout << titre << std::endl << auteur << std::endl;
    }
}