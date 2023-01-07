
def fonk():
    print("Hello world")
def ada(isim):
    print(isim+"Hoşgeldiniz")
def ada_2(isim:str):
    print(isim+"Hoşgeldiniz")
def topla(x1,x2):
    return x1+x2

def çift(x):
    if x%2==0:
        return True
    else:
        return False

#Verilen listeki verilen objenin kaç kere görüldüğünü bulan fonksiyon

def kaç(vliste,aranan):
    count=0
    for i in vliste:
        if i==aranan:
            count+=1
    return count
#print(kaç([3,4,"ali",["yeyo",3],("veli",0),"kebap",("veli",0)],("veli",0)))
#Verilen sayının bütün bölenlerini bir liste içinde veren bir fonksiyon
def bölen(x):
    liste=[]
    for i in range(1,x):
        if x%i==0:
            liste.append(i)
    return liste
#print(bölen(24))
#Verilen listeden en büyük ve en küçük tam sayıyı bulan fonksiyon(lar)
def büyük(lst):
    en=lst[0]
    for sayı in lst[1:]:
        if sayı>en:
            en=sayı
    return en
def küçük(lst):
    en=lst[0]
    for sayı in lst[1:]:
        if sayı<en:
            en=sayı
    return en
#print(küçük([2,7,4,9]))
#Verilen iki sayının en büyük ortak bölenini bulan fonksiyon
def ebob(sayi1,sayi2):
    ebob=1
    for i in range(1,küçük([sayi1,sayi2])+1):
        if sayi1%i==0 and sayi2%i==0:
            ebob=i
    return ebob
print(ebob(10,30))
#Bir listedeki iki indexteki objelerin yerini değiştiren bir fonksiyon yazalım
iste=["messi","cup","soup","pain","idea","anıl"]
def değiş(index1,index2,lst):
    temp=lst[index1]
    lst[index1]=lst[index2]
    lst[index2]=temp
    return lst
print(değiş(0,2,iste))
#Verilen listeyi küçükten büyüğe sıralayan bir fonksiyon yazalım
def sırala(lst):
    for x in range(len(lst)):
        for i in range(x+1,len(lst)):
            if lst[x]>lst[i]:
                lst=değiş(x,i,lst)
    return lst
#print(sırala([7,5,9,3,5,734,67,235576,45677764,3454]))
#Fonksiyonları kendi içindede çağırabiliriz. Örneğin fibanocci serisini yazalım
def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

