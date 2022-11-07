#include <iostream>
#include <cmath>
using namespace std;
 
int main()
{
   int populationActuelle;
   double croissancePourcent;
   cin >> populationActuelle >> croissancePourcent;
   int populationFuture = floor( populationActuelle * (1 + croissancePourcent / 100) );
   cout << populationFuture << endl;

}