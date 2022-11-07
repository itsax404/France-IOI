import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int numeroRecherché = entrée.nextInt();
        int tailleListe = entrée.nextInt();
        boolean trouvé = false;
        for(int i = 1; i <= tailleListe; i++){
            int numeroATesté = entrée.nextInt();
            if(numeroATesté == numeroRecherché){
                trouvé = true;
            }
        }
        if(trouvé){
            System.out.println("Sorti de la ville");
        }else{
            System.out.println("Encore dans la ville");
        }
    }
}
