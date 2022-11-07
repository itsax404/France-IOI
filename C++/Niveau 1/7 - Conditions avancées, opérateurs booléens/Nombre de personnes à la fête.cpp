#include <iostream>
using namespace std;

int main(){
    int nombrePersonnes, personnesPresentes = 0, personnesMax = 0;

    cin >> nombrePersonnes;

    for(int i = 1; i <= nombrePersonnes*2; i++){
        int action;
        cin >> action;

        if(action < 0){
            personnesPresentes--;
        }else{
            personnesPresentes++;
            if(personnesPresentes > personnesMax){
                personnesMax = personnesPresentes;
            }
        }
    }
    cout  << personnesMax << endl;


}