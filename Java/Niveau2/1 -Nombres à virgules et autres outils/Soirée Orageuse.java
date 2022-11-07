import algorea.Scanner;
import java.lang.Math;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        double secondes = entrée.nextDouble();
        double distanceMetre = secondes * 340.29;
        int kilometre = (int) Math.round(distanceMetre/1000);
        System.out.println(kilometre);
   }
}
