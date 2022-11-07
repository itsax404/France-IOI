import algorea.Scanner;

class Main{

    static Scanner entrée = new Scanner(System.in);
    
    public static void main(String[] args){
        int xMin = entrée.nextInt();
        int xMax = entrée.nextInt();
        int yMin = entrée.nextInt();
        int yMax = entrée.nextInt();
        int nombresMaison = entrée.nextInt();
        int maisonsSuspectes = 0;
        for(int i = 1; i <= nombresMaison; i++){
            int xMaison = entrée.nextInt();
            int yMaison = entrée.nextInt();

            if(((xMin <= xMaison) && (xMaison <= xMax)) && ((yMin <= yMaison) && (yMaison <= yMax))){
                maisonsSuspectes++;
            }
        }
        System.out.println(maisonsSuspectes);
    }
    
}
