import algorea.Scanner;

class Main{

    static  entrée = new Scanner(System.in);
    public static void main(String[] args){
        double épaisseur = 0.011;        
        for(int i = 1; i <= 15; i++){
           épaisseur *= 2;
        }
        print(épaisseur);
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
