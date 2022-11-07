import algorea.Scanner;
import java.lang.Math;


class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        double taxeActuelle = entrée.nextDouble();
        double nouvelleTaxe = entrée.nextDouble();
        double prixLégumes = entrée.nextDouble();
        double prixLégumesSansTaxes = prixLégumes/(1+taxeActuelle/100);
        double prixLégumesAvecTaxes = (double) Math.round((prixLégumesSansTaxes*(1+nouvelleTaxe/100) )* 100) / 100;
        System.out.println(prixLégumesAvecTaxes);
   }
}
