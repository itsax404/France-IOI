import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int nombre_maximum = entrée.nextInt();
        int nombre_pierres = 0;
        int étage = 0;
        while((nombre_maximum != 0) && (nombre_pierres + (étage+1)*(étage+1) <= nombre_maximum)){
            étage++;
            nombre_pierres += étage*étage;
        }

        print(étage);
        print(nombre_pierres);
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
