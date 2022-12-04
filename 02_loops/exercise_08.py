# Verilen tam sayı listesinde birbirine en yakın olan tamsayıların indexlerini bul.
import random
listem=random.sample(range(0, 10000000), 100)
indexler=[]
minuzaklık=10000
for sayı_i in range(len(listem)):
    for sayı_k in range(sayı_i+1,len(listem)):
        uzak=listem[sayı_k]-listem[sayı_i]
        if uzak<0:
            uzak=uzak*(-1)
        if uzak<=minuzaklık:
            minuzaklık=uzak
            indexler.append([sayı_i,sayı_k,uzak])
"""
cutoff=-len(indexler)+1
for geriye in range(-1,-len(indexler),-1):
    if indexler[geriye][2]<indexler[geriye-1][2]:
        cutoff=geriye
        break
cevap=indexler[-1:cutoff-1:-1]
"""
#Üstteki kod yerine loopta kullabiliriz.
cevap=[]
for i in range(-1,-len(indexler),-1):
    cevap.append(indexler[i])
    if indexler[i-1][2]>indexler[i][2]:
        break

print(cevap)
