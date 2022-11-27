# Kullanıcıdan 2 pozitif tamsayı alın. En büyük ortak bölenini bulun.
sayılar=input("Sayıları giriniz").split(",")
sayı1=int(sayılar[0])
sayı2=int(sayılar[1])
if sayı1<=sayı2:
    küçük=sayı1
else:
    küçük=sayı2
ebob=1
for i in range(2,küçük+1):
    if sayı1%i==0 and sayı2%i==0:
        ebob=i
print(ebob)