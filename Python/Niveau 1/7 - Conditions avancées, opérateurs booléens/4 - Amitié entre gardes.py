date_début_premier = int(input())
date_fin_premier = int(input())
date_début_second = int(input())
date_fin_second = int(input())

if (date_fin_second < date_début_premier) or (date_fin_premier < date_début_second):
  print("Pas amis")
else:
  print("Amis")