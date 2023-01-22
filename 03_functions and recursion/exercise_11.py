# Babylonian method bir sayının karekökünü yaklaşık hesaplamak için kullanılan bir algoritmadır.
# Bir tahminle başlar diyelim ki s_1 yaklaşık olarak sqrt(X).
#Sıradaki tahmin s_2=(s_1+X/s_1)/2  sqrt(X)'e daha yakındır.
#Algoritma s_n ile s_(n+1) yeterince yakın olduğunda biter.
#Verilen bir reel sayıyı istenilen ondalığa yuvarlayan bir fonksiyon yazınız.
# Babylonian methodu kullanrak verilen sayının karekökünü istenilen hassasiyete kadar bulan bir fonksiyon yazalım.

def BabylonianAlgoritması(number):
    if(number == 0):
        return 0
    q=number/2.0
    q_2=q+1
    while (q!=q_2):
        w=number/q
        q_2=q    
        q = (q + w)/2
    return q
print("4in karekökü=",BabylonianAlgoritması(82))