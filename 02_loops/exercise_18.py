#Kullanıcıdan iki sayı pozitif tam sayı alcaz. Biri v diğeri n.
# Yani (x1,x2,x3,...,xn) formundaki vectörlerden oluşan bir küme
#  ve xler 0 ile v arasında bir tam sayı.
# Bütün olası vectörleri içeren bir liste yaratınız.
# İpucu: tuple() fonksiyonu iterableları arraylere çevirir.
"""
sonuc=[]
n,v=input("Sayıları giriniz").split(",")
n,v=int(n),int(v)
tobe=[0 for _ in range(n)]
target=[v for _ in range(n)]
while tobe!=target:
    sonuc.append(tuple(tobe))
    tobe[0]+=1
    kay=0
    while tobe[kay]==v+1:
        tobe[kay]=0
        tobe[kay+1]+=1
        kay+=1
    
sonuc.append(tuple(target))
print(sonuc)
"""
