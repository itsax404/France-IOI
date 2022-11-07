import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nombreNotes = entrée.nextInt();
      int sommeNotes = 0;
      for (int loop = 1; loop <= nombreNotes; loop = loop + 1)
      {
         int note = entrée.nextInt();
         sommeNotes = sommeNotes + note;
      }
      // Trans-typage explicite
      System.out.println((double)sommeNotes / (double)nombreNotes);
   }
}
