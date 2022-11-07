import algorea.Scanner;

class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nombreOpérations = entrée.nextInt();
        int[] livres = new int[10];
        for(int i = 0; i < nombreOpérations; i++){
            int indexLivre = entrée.nextInt();
            int opération = entrée.nextInt();
            livres[indexLivre-1] += opération;
        }

        for(int x = 0; x < 10; x++){
            System.out.println(livres[x]);
        }
    }
}
