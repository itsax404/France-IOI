import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int nombreMesures = entrée.nextInt();
        int temperatureMinimum = entrée.nextInt();
        int temperatureMaximum = entrée.nextInt();
        boolean safe = true;
        int tour = 1;
        while((tour <= nombreMesures)){
            int mesure = entrée.nextInt();
            if((temperatureMinimum <= mesure) && (mesure <= temperatureMaximum)){
                print("Rien à signaler");
            }else{
                print("Alerte !!");
                safe = false;
                break;
            }
            tour++;
        }
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
