#Kullanıcıdan a,b,c,d sayıları al. ax^2+bx+c=d denklemini çöz. 
# Yaptığın işlemleri yazdır. Mesela
# b'yi a'ya böldüysen "b/a=sonucu" yazdır. a sıfısa eğer kullanıcıyı uyarsın.
#https://codeshare.io/WdwxWy
sayılar=input("ax\u00b2+bx+c=d denklemi için a,b,c,d'yi giriniz").split(",")
a=int(sayılar[0])
b=int(sayılar[1])
c=int(sayılar[2])
d=int(sayılar[3])
if a==0:
    print("Bu quadratic değil")
else:
    print(f"Denkleminiz:{a}x\u00b2+{b}x+{c}={d}  ")
    print(f"{c}-{d}={c-d}")
    print(f"Denkleminiz:{a}x\u00b2+{b}x+{c-d}=0 ")
    c=c-d
    print(f"{b}/{a}={b/a} ve {c}/{a}={c/a}")
    print(f"Denkleminiz:x\u00b2+{b/a}x+{c/a}=0 ")
    b=b/a
    c=c/a
    print(f"(x+{b/2})\u00b2=x\u00b2+{b}x+({b}/2)\u00b2=x\u00b2+{b}x+{(b/2)**2} ve -({b}/2)\u00b2+{c}={-((b/2)**2)+c} olduğuna göre")
    delta=((b/2)**2)-c
    sepe=b/2
    print(f"Denkleminiz: (x+{sepe})\u00b2={delta}")
    if delta<0:
        print("Bu denklemin reel çözümü yok.")
    elif delta==0:
        print("Bu denklemin tek çözümü var.")
        print(f"x={-sepe}")
    else:
        print("Bu denklemin 2 reel çözümü var.")
        print(f"x+{sepe}=\u221A{delta} veya x+{sepe}=-\u221A{delta}")
        print(f"x=-{sepe}+\u221A{delta} veya x=-{sepe}+\u221A{delta}")
        kök1=-sepe+delta**(1/2)
        kök2=-sepe-delta**(1/2)
        print(f"Kökler:{kök1},{kök2}")
