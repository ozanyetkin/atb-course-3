# İçinde stringler barındıran bir liste verildiğinde en çok karakter çeşidi olan
#  stringi dönen fonksiyon yazınız.
def çeşit(kelime:str):
    count=0
    for i in range(len(kelime)):
        if not kelime[i] in kelime[0:i]:
            count+=1
    return count
def finder(yazılistesi):
    find=yazılistesi[0]
    for a in yazılistesi[1:]:
        çeşit(a)