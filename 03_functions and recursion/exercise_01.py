#Bir poz. tam sayının bölenlerini bulan fonksiyon yazınız
def bölenler(x):
    liste=[]
    for i in range(1,x):
        if x%i==0:
            liste.append(i)
    return liste
#İki tamsaıy verilsin a,b. a=q*b+r eşitliğinde r bölümden kalan olcak şekilde q ve r yi veren fonksiyon yazalım
def bölüm(a,b):
    r=a%b
    q=a//b
    return q,r
#2 pozitif tam sayının ebob,ekok bulan fonksiyonlar yazın.İpucu: gcd(a,b)=gcd(b,r)
def gcd(a,b):
    if min(a,b)==0:
        return max(a,b)
    else:
        return gcd(b,a%b)
#gdc(a,b)*lcm(a,b)=a*b
def lcm(a,b):
    return (a*b)//gcd(a,b)
#Bir tam sayıdan küçük olan asal sayıları bulan fonksiyon yazınız.
primes=[2,3,5]
def prime_upto(x):
    denencek=[7,11]
    while primes[-1]<=x:
        for sayı in denencek:
            flag=True
            for prime in primes:
                if sayı%prime==0:
                    flag=False
            if flag:
                primes.append(sayı)
        denencek=[i+6 for i in denencek]
print(primes)
prime_upto(300)
print(primes)




#Bir tam sayının bütün asal çarpanlarının olduğu bir liste yaratan fonksiyonu yazalım.
#İpucu x'in asal çarpanları sqrt(x)'den küçük olmak zorunda.
#Bir tam sayıyı asal çarpanlarına ayıran fonksiyon yazınız.
