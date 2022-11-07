import algorea.Scanner;
import java.lang.Math;


class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int argent = entrée.nextInt();
        int prix = entrée.nextInt();
        int difference = argent / prix;
        System.out.println(difference);
   }
}
