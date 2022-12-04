# Kullanıcıdan bir sayı alın. Diyelimki x. x^x,x^2,x+x^2+x^3 değerini bulun.
# En büyük değerin hangi fonksiyona ait olduğunu söyleyin.
#Değerleri aynı sırada, yüzdelik değere (noktadan sonra 2 karakter) kadar yazdırın.
x=float(input("Bir sayı giriniz"))
üstel=x**x
kare=x**2
poli=x+x**2+x**3

if üstel>=kare:
    if üstel>=poli:
        print("x^x",round(üstel,2),round(kare,2),round(poli,2))
    else:
        print("x+x^2+x^3",round(üstel,2),round(kare,2),round(poli,2))
else:
    if kare>=poli:
        print("x^2",round(üstel,2),round(kare,2),round(poli,2))
    else:
        print("x+x^2+x^3",round(üstel,2),round(kare,2),round(poli,2))