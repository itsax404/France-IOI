import algorea.Scanner;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int[] ingrédients = {9,5,12,15,7,42,13,10,1,20};
        int somme = 0;
        for(int i = 0; i < 10; i++){
            int nombreKilos = entrée.nextInt();
            somme += nombreKilos*ingrédients[i];
        }
        System.out.print(somme);

    }
}
