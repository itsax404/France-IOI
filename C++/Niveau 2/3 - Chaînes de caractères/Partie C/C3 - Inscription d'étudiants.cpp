#include <iostream>
#include <string>

int main(){
    std::string nomEtudiant;
    std::cin  >> nomEtudiant;
    char premiereLettre = nomEtudiant[0];
    if(premiereLettre < 'G'){
        std::cout << 1 << std::endl;
    }else if(premiereLettre < 'Q'){
        std::cout << 2 << std::endl;
    }else{
        std::cout << 3 << std::endl;
    }
    
}