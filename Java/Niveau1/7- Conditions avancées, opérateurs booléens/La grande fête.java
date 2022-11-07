import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int dateDebut = entrée.nextInt();
        int dateFin = entrée.nextInt();
        int nombreInvités = entrée.nextInt();
        int invitésSuspects = 0;
        for(int i = 1; i <= nombreInvités; i++){
            int dateArrivé = entrée.nextInt();
            int dateDépart = entrée.nextInt();
            boolean innoncent = ((dateDépart < dateDebut) || (dateArrivé > dateFin))
            if(!innoncent){
                invitésSuspects++;
            }
        }
        
        System.out.println(invitésSuspects);
        
    }
}
