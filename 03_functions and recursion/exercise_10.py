#Bir yazı verildiğinde bu yazıyı kısaltan bir fonksiyon yazmak istiyoruz.
# Örneğin  AAAA4ZZCY yi  #4A4ZZCY olarak yazarsak 1 karakter kısaltmıs oluruz.
#Bu metodu kullanarak yazıyı kısaltan bir fonksiyon yazınız
def kısalt_1(yazı):
    yazı+="*"
    kısalmıs=""
    count=1
    for i in range(1,len(yazı)):
        if yazı[i]==yazı[i-1]:
            count+=1
        else:
            if count>3:
                kısalmıs+="#"+str(count)+yazı[i-1]
            else:
                kısalmıs+=yazı[i-1]*count
            count=1
        if count==10:
            kısalmıs+="#9"+yazı[i-1]
            count=1
    return kısalmıs
print(kısalt_1("AAAA444444444444ZZCY"))  

# 9 dan fazla tekrar eden karakterler için #sayı/X formatını kullanan bir fonksiyon yazalım.
#Yani #9A#9A yerine #18/A gelcek.
def kısalt_2(yazı):
    yazı+="*"
    kısalmıs=""
    count=1
    for i in range(1,len(yazı)):
        if yazı[i]==yazı[i-1]:
            count+=1
        else:
            if count<4:
                kısalmıs+=yazı[i-1]*count
            elif count<10:
                kısalmıs+="#"+str(count)+yazı[i-1]
            elif count==10:
                kısalmıs+="#9"+yazı[i-1]
            else:
                kısalmıs+="#"+str(count)+"/"+yazı[i-1]
            count=1
    return kısalmıs
print(kısalt_2("AAAAAAAAABBBBBBBBBBBCCCCCCCCCCCCCCCC"))






