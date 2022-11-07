import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int nombresPersonnes = entrée.nextInt();
        for(int i = 1; i <= nombresPersonnes; i++){
            int taille = entrée.nextInt();
            int age = entrée.nextInt();
            int poids = entrée.nextInt();
            int cheval = entrée.nextInt();
            int cheveuxBruns = entrée.nextInt();
            int critères = 0;
            if((taille <= 182) && (taille >= 178)){
                critères++;
            }
            if(age >= 34){
                critères++;            
            }
            if(poids < 70){
                critères++;
            }
            if(cheval == 0){
                critères++;
           }
           if(cheveuxBruns == 1){
                critères++;
            }

            if (critères == 5){
                print("Très probable");
            }else if( critères == 0){
                print("Impossible");
            }else if((critères == 3) || (critères == 4 )){
                print("Probable");
            }else{
                print("Peu probable");
            }

        }
        
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
