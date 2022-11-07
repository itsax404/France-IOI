#include <iostream>

using namespace std;

int main(){

    int superficieArignon, superficieEvaran;
    cin >> superficieArignon >> superficieEvaran;

    if(superficieArignon > superficieEvaran){
        int difference = superficieArignon - superficieEvaran;
        if(difference > 10){
            cout << "La famille Arignon a un champ trop grand" << endl;
        }
    }else{
        int difference = superficieEvaran - superficieArignon;
        if(difference > 10){
            cout << "La famille Evaran a un champ trop grand" << endl;
        }
    }

}