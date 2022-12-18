#Sezar şifrelemesi:Size verilen 
# yazıdaki her karakteri alfabede n kaydırarak elde edilen karakterle değiştiriniz.
# n sayısını kullanıcıdan alın.
alfabe=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key=int(input("Anahtarı giriniz"))
mesaj=input("Şifrelenicek mesajı giriniz")
şifrelenmiş=""
"""
for i in mesaj:
    for e in range(len(alfabe)):
        if i == alfabe[e]:
            if e+key>len(alfabe):
                şifrelenmiş+=alfabe[e+key-len(alfabe)]
            else:
                şifrelenmiş+=alfabe[e+key]
"""
#key (anahtar) 26'dan büyük olabilsin istiyoruz
"""
for i in mesaj:
    for e in range(len(alfabe)):
        if i == alfabe[e]:
            şifrelenmiş+=alfabe[(key+e)%len(alfabe)]
"""   
#enumerate fonksiyonunu kullanabiliriz
for i in mesaj:
    for e,harf in enumerate(alfabe):
        if i == harf:
            şifrelenmiş+=alfabe[(key+e)%len(alfabe)]
print(şifrelenmiş)