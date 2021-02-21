# -*- coding: utf-8 -*-
"""ödev2.ipynb
"""

Students=[]
S1 = input("Öğrencinin isim ve soyismini giriniz:").upper()
S2 = input("Öğrencinin isim ve soyismini giriniz:").upper()
S3 = input("Öğrencinin isim ve soyismini giriniz:").upper()
S4 = input("Öğrencinin isim ve soyismini giriniz:").upper()
S5 = input("Öğrencinin isim ve soyismini giriniz:").upper()
Students.append(S1)
Students.append(S2)
Students.append(S3)
Students.append(S4)
Students.append(S5)

print("\nStudents:",Students,end='\n')
midterm = []    
final = []   
homework = []
  
midterm = [int(i) for i in input("Sırayla öğrencilerin midterm notları: ").split(",")] 
final = [int(x) for x in input("Sırayla öğrencilerin final notları: ").split(",")] 
homework = [int(j)for j in input("Sırayla öğrencilerin ödev notları: ").split(",")]

print("\nmidterm:",midterm) 
print("final:",final) 
print("homework:",homework)

s1notları= (midterm[0],final[0],homework[0])
s2notları= (midterm[1],final[1],homework[1])
s3notları= (midterm[2],final[2],homework[2])
s4notları= (midterm[3],final[3],homework[3])
s5notları= (midterm[4],final[4],homework[4])

information={S1:s1notları,S2:s2notları,S3:s3notları,S4:s4notları,S5:s5notları}

print("\nÖğrencilerin sırayla midterm,final ve homework notları:",information)
grades=[]
for i in information.values():
	grades.append(i)
ort={}
ort[(grades[0][0]+grades[0][1]+grades[0][2])/3]=S1
ort[(grades[1][0]+grades[1][1]+grades[1][2])/3]=S2
ort[(grades[2][0]+grades[2][1]+grades[2][2])/3]=S3
ort[(grades[3][0]+grades[3][1]+grades[3][2])/3]=S4
ort[(grades[4][0]+grades[4][1]+grades[4][2])/3]=S5

ortalama=sorted(ort.items())
print("\nÖğerencilerin ortalamaları:",ortalama)
print(ortalama[4][0],"ortalama ile",ortalama[4][1],"birinci. TEBRİKLER!")
