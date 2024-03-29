#Faktoriyel alan fonksiyon yazınız.
#Recursive olan:
"""
def factor(n:int):
    if n>1:
        return n*factor(n-1)
    else:
        return 1
"""
def factor(n):
    ft=1
    for i in range(2,n+1):
        ft*=i
    return ft

# Verilen [[c,x1,x2,x3,x4,x5,x6..,xn],x] tamsayı listesini c+x1*x+x2*x^2+x3*x^3..+xn*x^n=f(x) polinomu olarak düşünüp f(x) yi veren bir fonksiyon yazınız.
def eva_polinom(girdi):
    katsayılar=girdi[0]
    değer=girdi[1]
    toplam=katsayılar.pop(0)
    for üs,kat in enumerate(katsayılar):
        toplam+=kat*değer**(üs+1)
    return toplam

#f(x)=1+3*x^2, f(3)=1+3*3**2=1+3*9=28
#print(eva_polinom([[1,0,3],3]))

# Yukarıdaki notasyonla verilen [c,x1,x2,...xn] listesini alıp f(x) fonksiyonunu veren bir fonksiyon yazınız.
def pol_generator(poli_lst):
    def polinom(x):
        return eva_polinom([poli_lst,x])
    return polinom

benim_pol=pol_generator([1,0,3])
#print(benim_pol(3))

# e^x,sin(x),cos(x) fonksiyonlarının sonsuz serilerini belli bir değere kadar hesaplayan fonksiyonlar yazınız. 
def func_e(x,lmt):
    pol=pol_generator([1/factor(i) for i in range(lmt)])
    return pol(x)
#Daha hızlı
"""
def func_e(x, lmt):
    term=1
    hesap=0
    for i in range(1,lmt):
        carp=x/i
        hesap+=term
        term*=carp
    return hesap
"""
print(func_e(1,50))
# e^x,sin(x),cos(x) fonksiyonlarının istenilen hata payıyla hesaplayan fonksiyonlar yazınız.
