import algorea.Scanner;
import java.lang.Math;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        double quantitéCiment = entrée.nextDouble();
        int nombreSacCiments = (int) Math.ceil(quantitéCiment/60);
        int prixCiment = nombreSacCiments*45;
        System.out.println(prixCiment);
   }
}
