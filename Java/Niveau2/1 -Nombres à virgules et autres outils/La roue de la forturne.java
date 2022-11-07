import algorea.Scanner;



class Main{
   public static void main(String[] args){
        Scanner entrée = new Scanner(System.in);
        int nbZones = entrée.nextInt();
        System.out.println(((nbZones % 24) + 24 ) % 24);
    }
}
