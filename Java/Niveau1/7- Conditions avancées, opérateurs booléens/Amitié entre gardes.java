import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);

    public static void main(String[] args){
        int soldat1Debut = entrée.nextInt();
        int soldat1Fin = entrée.nextInt();
        int soldat2Debut = entrée.nextInt();
        int soldat2Fin= entrée.nextInt();

        if(((soldat2Debut >= soldat1Debut) && (soldat2Debut <= soldat1Fin)) || ((soldat2Fin >= soldat1Debut) && (soldat2Fin <= soldat1Fin)) || ((soldat1Debut >= soldat2Debut) && (soldat1Debut <= soldat2Fin))){
            print("Amis");
        }else{
            print("Pas amis");
        }

    }

    private static void print(String args){
        System.out.println(args);
    }

}