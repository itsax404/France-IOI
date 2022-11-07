import algorea.Scanner;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int[] ingrédients = {500,180,650,25,666,42,421,1,370,211};
        int indexIngrédient = entrée.nextInt();
        System.out.print(ingrédients[indexIngrédient]);
    }
}
