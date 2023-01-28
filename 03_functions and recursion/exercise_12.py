#Bir tam sayı listesi veriliyor.
#Bu tam sayılar listesindeki sayıların toplamının karesiyle karelerinin toplamı arasındaki
#farkı bulan bir fonksiyon yazınız.
#Basit yaklaşım
"""
def topla(lst):
    toplam=0
    for i in lst:
        toplam+=i
def kare(lst):
    sqst=[]
    for i in lst:
        sqst.append(i*i)
def sonuc(lst):
    topkare=topla(lst)**2
    karetop=topla(kare(lst))
    return abs(topkare-karetop)
"""
