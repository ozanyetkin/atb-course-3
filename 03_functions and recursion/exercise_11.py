# Babylonian method bir sayının karekökünü yaklaşık hesaplamak için kullanılan bir algoritmadır.
# Bir tahminle başlar diyelim ki s_1 yaklaşık olarak sqrt(X).
#Sıradaki tahmin s_2=(s_1+X/s_1)/2  sqrt(X)'e daha yakındır.
#Algoritma s_n ile s_(n+1) yeterince yakın olduğunda biter.
#Verilen bir reel sayıyı istenilen ondalığa yuvarlayan bir fonksiyon yazınız.
# Babylonian methodu kullanrak verilen sayının karekökünü istenilen hassasiyete kadar bulan bir fonksiyon yazalım.
def yuvarla(sayı,hassa):
    kay=sayı*(10**(hassa+1))
    if int(kay)%10<5:        
        return int(kay/10)/(10**(hassa))
    else:
        return (int(kay/10)+1)/(10**(hassa))
#print(yuvarla(7.34547465734647,7))
def next_s(sayı,X):
    return sayı/2+X/(2*sayı)
def babylo(X,hassa):
    kutu1=X/2
    kutu2=next_s(kutu1,X)
    while yuvarla(kutu1,hassa)!=yuvarla(kutu2,hassa):
        kutu1=kutu2
        kutu2=next_s(kutu1,X)
    return yuvarla(kutu1,hassa)

print(82**(1/2))




