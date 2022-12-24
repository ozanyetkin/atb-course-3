# Verilen bir yazıda alfabedeki her karakterin görülme sıklığını bulunuz.
#Alfabe listesindeki harflere karşılık gelen sıklıkların içinde bulunduran bir liste yazdırın.

alfabe=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
yazı=input("Yazıyı giriniz")
"""
lst=[]
for karak in alfabe:
    count=0
    for char in yazı:
        if karak==char:
            count+=1
    lst.append(count)
sonuc=[x/len(yazı) for x in lst]
print(sonuc)

"""
lst=[]
uzu=len(yazı)
for karak in alfabe:
    count=0
    for char in yazı:
        if karak==char:
            count+=1
    lst.append(count/uzu)
# Normalde 1 den 10 kadar olan sayıların listesin yaparken
ct=[]
for i in range(1,11):
    ct.append(i)
print(ct)
#Bir diğer yolu
ct=[i for i in range(1,11)]
print(ct)
# İstiyorumki ct'nin içindeki sayılara 1 ekliyelim
for i in range(len(ct)):
    ct[i]+=1
print(ct)
#Başka bir yolu
ct=[x+1 for x in ct]
print(ct)
#Çift sayılar "a" olsun tek sayılar "b" olsun:
ct=["a" if x%2==0 else "b" for x in ct]
print(ct)
