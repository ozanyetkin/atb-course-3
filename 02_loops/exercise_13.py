# Bir liste verilmiş olsun. Bu listenin içindeki objeleri indexleriyle beraber içeren bir liste oluşturcaz.
#  Oluşturcağımız listenin içinde 2 elemanlı arrayler olsun istiyoruz. Verilen liste [a,b] ise oluşturmak istediğimiz liste [(0,a),(1,b)] olcak.
liste=["ali","veli",5,True,["heyyo","meyyo"]]
sonuc=[]

a=0
for obj in liste:
    sonuc.append((a,obj))
    a+=1
print(sonuc)
"""

for i in range(len(liste)):
    sonuc.append((i,liste[i]))
print(sonuc)
"""
"""
for tpl in enumerate(liste):
    print(tpl)
"""
"""
for index,obj in enumerate(liste):
    print(index)
    print(obj)
"""