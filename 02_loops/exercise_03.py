#Kullanıcıdan pozitif tam sayı alın. Faktoriyelin bulup yazdırın. n ise n!'i arıyoruz.
n=int(input("Sayıyı giriniz"))
faktör=1
for i in range(2,n+1):
    faktör*=i
print(faktör)
    