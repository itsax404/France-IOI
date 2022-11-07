import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int chiffre = 0;
        int somme = 0;
        while(chiffre != -1){
            int nombre = entrée.nextInt();
            if(nombre == -1){
                break;
            }
            chiffre = nombre;
            somme += chiffre;
        }
        print(somme);
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
