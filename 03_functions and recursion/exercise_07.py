# 2 arabanın hız, konum ve ivme değerleri veriliyor.
#Geriden gelen araba (pozitif x yönü) öndekini hiç yakalar mı söyleyen bir fonksiyon yazalım.
#Zamanı saniye saniye modelleyelim.
araba_1=[3,6,2]
araba_2=[6,0,5]
def geçer(ara1,ara2):
    if ara1[0]>ara2[0]:
        öndeki=ara1
        arkadaki=ara2
    else:
        öndeki=ara2
        arkadaki=ara1
    if öndeki[2]<arkadaki[2]:
        #arkadaki daha ivmeliyse elinde sonunda geçer
        return True
    elif  öndeki[2]==arkadaki[2]:
        #Eşit ivmeliyse hız bakarız
        if arkadaki[1]<=öndeki[1]:
            #Öndeki daha hızlı veya eşit hızlıysa hiç yakalayamaz
            return False
        else:
            #Arkadaki daha hızlıysa elinde sonunda yakalar
            return True
    elif öndeki[1]>=arkadaki[1]:
        #Öndeki daha ivmeliyse arkadaki en azından daha hızlı olmalı
        return False
    else:
        rel_konum=öndeki[0]-arkadaki[0]
        rel_hız=öndeki[1]-arkadaki[1]
        rel_ivme=öndeki[2]-arkadaki[2]
        while rel_konum>0:
            rel_konum+=rel_hız
            rel_hız+=rel_ivme
            if rel_hız>0:
                return False
        return True


    
    

    

