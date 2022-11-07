import java.util.ArrayList;
import java.util.List;

import algorea.Scanner;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nombreDéplacements = entrée.nextInt();
        int[] déplacements = new int[nombreDéplacements];
        for(int x = 0; x < nombreDéplacements; x++){
            déplacements[x] = entrée.nextInt();
        }

        for (int x = nombreDéplacements; x > 0; x--){
            int déplacement = déplacements[x-1];
            
            switch(déplacement){
                case 1:
                    System.out.println(2);
                    break;
                case 2:
                    System.out.println(1);
                    break;
                case 3:
                    System.out.println(3);
                    break;
                case 4:
                    System.out.println(5);
                    break;
                case 5:
                    System.out.println(4);
                    break;
                default:
                    break;
            }
        }
    }
}
