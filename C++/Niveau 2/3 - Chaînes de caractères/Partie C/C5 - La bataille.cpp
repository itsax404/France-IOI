#include <iostream>
#include <string>

int main(){
    std::string ligneJoueur1, ligneJoueur2;
    std::cin >> ligneJoueur1;
    std::cin >> ligneJoueur2;

    if(ligneJoueur1.size() < ligneJoueur2.size()){
        int egalite = 0;
        for(int i = 0; i < ligneJoueur1.size(); i++){
            if(ligneJoueur1[i] == ligneJoueur2[i]){
                egalite++;
            }else if(ligneJoueur1[i] < ligneJoueur2[i]){
                std::cout << egalite << std::endl << 1;
                std::exit(1);
            }else{
                std::cout << egalite << std::endl << 2;
                std::exit(1);
            }
            std::cout << egalite << std::endl << 2;
            std::exit(1);
        }
    }else if(ligneJoueur1.size() > ligneJoueur2.size()){
        int egalite = 0;
        for(int i = 0; i < ligneJoueur2.size(); i++){
            if(ligneJoueur2[i] == ligneJoueur2[i]){
                egalite++;
            }else if(ligneJoueur1[i] < ligneJoueur2[i]){
                std::cout << egalite << std::endl << 1;
                std::exit(1);
            }else{
                std::cout << egalite << std::endl << 2;
                std::exit(1);
            }
            std::cout << egalite << std::endl << 1;
            std::exit(1);
        }
    }else{
        int egalite = 0;
        for(int i = 0; i < ligneJoueur1.size(); i++){
            if(ligneJoueur1[i] == ligneJoueur2[i]){
                egalite++;
            }else if(ligneJoueur1[i] < ligneJoueur2[i]){
                std::cout << egalite << std::endl << 1;
                std::exit(1);
            }else{
                std::cout << egalite << std::endl << 2;
                std::exit(1);
            }
            std::cout << egalite << std::endl << "=";
            std::exit(1);
        }
    }
}