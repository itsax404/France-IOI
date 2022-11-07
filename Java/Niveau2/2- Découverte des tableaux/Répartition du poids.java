import java.util.ArrayList;
import java.util.List;

import algorea.Scanner;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nombreCharettes = entrée.nextInt();
        List<Double> poidsCharettes = new ArrayList<>();

        for(int i = 0; i < nombreCharettes; i++){
            double poidsCharette = entrée.nextDouble();
            poidsCharettes.add(poidsCharette);
        }

        double poidsTotal = (double) 0;
        for(int i = 0; i < nombreCharettes; i++){
            poidsTotal += poidsCharettes.get(i);
        }

        double poidsParCharette = poidsTotal/nombreCharettes;

        for(int i = 0; i < nombreCharettes; i++){
            System.out.println(poidsParCharette - poidsCharettes.get(i));
        }

    }
}
