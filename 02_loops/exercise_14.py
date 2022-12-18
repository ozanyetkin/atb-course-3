#Kullanıcıdan "bitti" yazana kadar sayı isteyen bir kod yazınız. 
# Eğer sayı girmesse uyarsın ve tekrar sorsun. Verdiği sayıları bir listeye ekleyin. Sayı vermesse uyarın
# "bitti" yazıncada verdiği yazıların olduğu listeyi yazdırın. Stringlerde 
#  tanımlı .isnumeric() fonksiyonu eğer verilen yazı sayıya çevrilebilir değilse false verir.
girdi=input("Sayı veriniz")
listesi=[]
while girdi!="bitti":
    if girdi.isnumeric():
        listesi.append(girdi)
        girdi=input("İsterseniz tekrar sayı giriniz yada bitti yazınız")
    else:
        girdi=input("Yanlış giriş yaptınız yeni sayı veriniz yada bitti yazınız.")
print(listesi)
