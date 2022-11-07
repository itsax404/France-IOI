import algorea.Scanner;
import static java.util.Arrays.*;
class Main
{
   public static void main(String[] args)
   {

    /**
     * Ne pas copier, ne marche pas !
     */
    Scanner entrée = new Scanner(System.in);
    int nombrePersonnes= entrée.nextInt();
    int [] participants = new int[nombrePersonnes];
    for (int idPersonne = 0; idPersonne < nombrePersonnes; idPersonne = idPersonne + 1)
    {
        participants[idPersonne] = entrée.nextInt();
    }
    
    sort(participants);
    for(int x = 0; x < nombrePersonnes/2; x ++){
        System.out.printf("%d %d",participants[x], participants[(participants.length-1)-x]);
        System.out.println();
    }
}
}