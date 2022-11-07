import algorea.Scanner;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nombreProduits = entrée.nextInt();
        int[] listeProduits = new int[nombreProduits];
        int nombrePersonnes = entrée.nextInt();
        for(int i = 0; i <nombrePersonnes; i++){
            int indexProduitPréféré = entrée.nextInt();
            listeProduits[indexProduitPréféré] ++;
        }

        for(int x = 0; x < nombreProduits; x++){
            System.out.println(listeProduits[x]);
        }
    }
}
