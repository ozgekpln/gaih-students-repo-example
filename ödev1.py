# -*- coding: utf-8 -*-
"""ödev1.ipynb
"""

asalSayılar=set(asalSayılar)
for i in range(1,101):
  if i>1:
    for j in range(2,i):
      if(i % j)==0:
        break
    else:
      asalSayılar.add(i)
matris=[[0 for x in range(3)]for y in range(3)] 

for k in range(3):
   for z in range(3):
     for d in asalSayılar:
       matris[k][z]=d 
     asalSayılar.remove(d) 
for r in matris:        
  print(r)
