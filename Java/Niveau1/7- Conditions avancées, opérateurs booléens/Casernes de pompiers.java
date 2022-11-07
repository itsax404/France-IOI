import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int pairesZones = entrée.nextInt();
        for(int i = 1; i <= pairesZones; i++){
            int xMinA = entrée.nextInt();
            int xMaxA = entrée.nextInt();
            int yMinA = entrée.nextInt();
            int yMaxA = entrée.nextInt();
            int xMinB = entrée.nextInt();
            int xMaxB = entrée.nextInt();
            int yMinB = entrée.nextInt();
            int yMaxB = entrée.nextInt();
            if((xMinB >= xMaxA) || (xMaxB <= xMinA) || (yMinB >= yMaxA) ||(yMaxB <= yMinA)){
                System.out.println("NON");
            }else{
                System.out.println("OUI");
            }
        }
    }
}
