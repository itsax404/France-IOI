import algorea.Scanner;
import java.lang.Math;


class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nombrePersonnes = entrée.nextInt();
        int nombreFruits = entrée.nextInt();
        int difference = nombreFruits % nombrePersonnes;
        if(difference == 0){
            System.out.println("oui");
        }else{
            System.out.println("non");
        }
        
   }
}
