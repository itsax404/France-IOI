import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);

    public static void main(String[] args){
        int nombreMarchands = entrée.nextInt();
        
        int meilleurMarchands = 0;
        int prixMeilleurMarchands = 1000000000;
        for(int i = 1; i <= nombreMarchands; i++){
            int prixMarchands = entrée.nextInt();
            if(prixMarchands <= prixMeilleurMarchands){
                prixMeilleurMarchands = prixMarchands;
                meilleurMarchands = i;
            }
        }
        System.out.print(meilleurMarchands);

    }

}