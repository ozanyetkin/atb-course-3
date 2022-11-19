# Kullanıcıdan iki sayı alın x,y şeklinde. Eğer toplamları 15 ile 30
#  arasıdnaysa 30 değilse doğru değeri yazdırınız.
sayılar=input("Sayıları giriniz")
sayılar=sayılar.split(",")
ilksayı,ikincisayı=int(sayılar[0]),int(sayılar[1])
toplam=ilksayı+ikincisayı
if 15<toplam<30:
    print(30)
else:
    print(toplam)
