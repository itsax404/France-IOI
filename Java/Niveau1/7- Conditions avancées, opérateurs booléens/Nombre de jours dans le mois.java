import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);

    public static void main(String[] args){
        int mois = entrée.nextInt();
        int jours = 0;
        if(mois == 11){
            jours = 29;
        }else if((4 <= mois) && (mois <= 6) || (mois == 10)){
            jours = 31;
        }else{
            jours = 30;
        }
        System.out.print(jours);

    }
}