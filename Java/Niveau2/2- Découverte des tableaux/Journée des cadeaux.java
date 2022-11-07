import algorea.Scanner;
import static java.util.Arrays.*;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbPersonnes = entrée.nextInt();
      int [] fortune = new int[nbPersonnes];
      for (int idPersonne = 0; idPersonne < nbPersonnes; idPersonne = idPersonne + 1)
      {
         fortune[idPersonne] = entrée.nextInt();
      }
       
      sort(fortune);
       
      if ((nbPersonnes % 2) == 1)
      {
         int milieu = (nbPersonnes - 1) / 2;
         System.out.println( fortune[milieu] );
      }
      else
      {
         int milieu = nbPersonnes / 2;
         System.out.println( (double)( fortune[milieu - 1] + fortune[milieu] ) / 2 );
      }
   }
}