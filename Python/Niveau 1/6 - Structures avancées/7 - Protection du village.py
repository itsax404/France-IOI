perimetre=0 
nombre_maisons = int(input()) 
xmin=1000000000 
xmax=0 
ymin=1000000000 
ymax=0 
for loop in range(nombre_maisons): 
   x=int(input()) 
   y=int(input()) 
   if x < xmin: 
      xmin=x 
   if x > xmax:
      xmax=x
   if y < ymin:
      ymin=y 
   if y > ymax: 
      ymax=y 
   perimetre=2*((xmax-xmin)+(ymax-ymin)) 
print(perimetre)