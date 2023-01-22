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
    for yazı in yazılistesi[1:]:
        if çeşit(yazı)>çeşit(find):
            find=yazı
    return find
string_list = ["Hello World", "1234567890", "abcdefghijklmnopqrstuvwxyz"]
sa = finder(string_list)
print(sa)