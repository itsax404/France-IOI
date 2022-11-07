import algorea.Scanner;

class Main{

    static Scanner entrée = new Scanner(System.in);
    public static void main(String[] args){
        int nombreLégumes = entrée.nextInt();
        for(int i = 1;i <= nombreLégumes; i++){
            double poids = entrée.nextDouble();
            double age = entrée.nextDouble();
            double prixVente = entrée.nextDouble();
            double prixAuKilo = prixVente / poids;
            print(prixAuKilo);
        }
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
