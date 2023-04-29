#include <iostream>
#include <string.h>

int main(){

    for(int idLigne; idLigne < 2; idLigne++){
        char ligne[101];
        std::scanf("%[^\n]\n", ligne);
        for(int i = 0; i < strlen(ligne); i++){
            char lettre = ligne[i];
            if(lettre != ' ' && lettre != 'A' && lettre != 'E' && lettre != 'I' && lettre != 'O' && lettre != 'U' && lettre != 'Y'){
                std::printf("%c", lettre);
            }
        }
        std::printf("\n");
    }

}