import java.util.HashMap;

import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int nombrePersonnes = entrée.nextInt();
        int personnes = 0;
        int personnesMax = 0;
        for(int i = 1; i <= nombrePersonnes*2; i++){
            int chiffre = entrée.nextInt();
            if(chiffre > 0){
                personnes++;
            }else if(chiffre < 0){
                personnes--;
            }
            if(personnesMax < personnes){
                personnesMax = personnes;
            }
        }
        System.out.println(personnesMax);
    }
}
