
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
print(bölen(24))
#Verilen listeden en büyük ve en küçük tam sayıyı bulan fonksiyon(lar)
#Verilen iki sayının en büyük ortak bölenini bulan fonksiyon