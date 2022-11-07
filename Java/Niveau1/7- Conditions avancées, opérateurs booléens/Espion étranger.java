import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);

    public static void main(String[] args){
        int dateDebut = entrée.nextInt();
        int dateFin = entrée.nextInt();
        int nombreEntrées = entrée.nextInt();
        int personnesSuspectes = 0;
        for(int i = 1; i <= nombreEntrées; i++){
            int dateEntree = entrée.nextInt();
            if((dateDebut <= dateEntree) && (dateEntree <= dateFin)){
                personnesSuspectes++;
            }
        }
        System.out.println(personnesSuspectes);
    }
}