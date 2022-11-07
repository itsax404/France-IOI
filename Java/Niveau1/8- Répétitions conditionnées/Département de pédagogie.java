import algorea.Scanner;

class Main{
    static Scanner entrée = new Scanner(System.in);     

    public static void main(String[] args){
        int nombre = entrée.nextInt();
        int nombre_proposition = 0;
        int proposition = 1000;
        while(proposition != nombre){
           proposition = entrée.nextInt();
            if(proposition == nombre){
                nombre_proposition++;
                print("Nombre d'essais nécessaires :");
                print(nombre_proposition);
                break;
            }else if (proposition < nombre){
                print("c'est plus");
                nombre_proposition++;
            }else if (proposition > nombre){
                print("c'est moins");
                nombre_proposition++;
            }
        }
    }

    private static void print(Object object){
        System.out.println(object);
    }
}
