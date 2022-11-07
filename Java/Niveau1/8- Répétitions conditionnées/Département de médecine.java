import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int population = entrée.nextInt();
        int malade = 1;
        int jour = 1;
        while(malade < population){
            malade += 2;
            jour++;
        }
        print(jour);
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
