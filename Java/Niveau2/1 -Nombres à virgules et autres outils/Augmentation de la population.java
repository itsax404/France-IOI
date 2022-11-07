import algorea.Scanner;
import java.lang.Math;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nombrePersonnes = entrée.nextInt();
        double pourcentage = entrée.nextDouble();
        int nombrePopulation = (int) Math.floor(nombrePersonnes*(1+pourcentage/100));
        System.out.println(nombrePopulation);
   }
}
