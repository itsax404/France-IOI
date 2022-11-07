import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int nombreCoordonnées = entrée.nextInt();
        for(int i = 1; i <= nombreCoordonnées; i++){
            int xJeton = entrée.nextInt();
            int yJeton = entrée.nextInt();
            boolean dansFeuille = (((xJeton > 0) && (xJeton < 90)) && ((yJeton > 0) && (yJeton < 70)));
            boolean dansZoneJauneMilieu = (((xJeton > 25) && (xJeton < 50)) && ((yJeton > 20) && (yJeton < 45)));
            if(!dansFeuille){
                print("En dehors de la feuille");
            }else if((yJeton < 60) && (((xJeton < 15) && (xJeton < 45)) || ((xJeton > 60) && (xJeton < 85)))){
                print("Dans une zone rouge");
            }else if((!dansZoneJauneMilieu) && ((xJeton > 10) && (xJeton < 85)) && ((yJeton > 10) && (yJeton < 55))){
                print("Dans une zone bleue");
            }else{
                print("Dans une zone jaune")
            }
        }
        
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
