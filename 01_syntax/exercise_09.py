#Kullanıcıdan 10 ile 100 arasında bir sayı alın. Yanış verirse uyarın. Diyelimki sayı ab.
#Sonra kullanıcıdan bir kelime alın. Kelimenin a ve b 'inci indexindeki karakterleri bulun.
# Eğer ilk karakter s ise yazının yanına kopyalanmıs halini yazdırın. Eğer değilse ve ikinci karakter
# t ise yazının başına lt ekleyip yazdırın. Eğer l ise sonuna tl ekleyip yazdırın. İkiside değilse
# Yazının son harfini başına ekleyip yazdırın.

# https://codeshare.io/WdwxWy
"""
Test için
100--Uyarı
9--Uyarı
34,muzlukek--kmuzlukek
34,muzsuzkek--muzsuzkekmuzsuzkek
35,muzlutekerlek--ltmuzlutekerlek
37,çileklilimon--çileklilimontl
9,muzlukek--Uyarı
"""
#Uzun kod:
"""
sayı=input("10'la 100 arasında bir sayı gir")

if int(sayı)<10 or int(sayı)>=100:
    print("yanlış sayı girdiniz")
else:
    kelime=input("Kelimeyi gir")
    ilk=kelime[int(sayı[0])]
    iki=kelime[int(sayı[1])]
    if ilk == "s":
        print(kelime+kelime)
    else:
        if iki =="t":
            print("lt"+kelime)
        else: 
            if iki == "l":
                print(kelime+"tl")
            else: 
             print(kelime[-1]+kelime)
"""
#Kısa kod:
    
sayı=input("10'la 100 arasında bir sayı gir")

if int(sayı)<10 or int(sayı)>=100:
    print("yanlış sayı girdiniz")
else:
    kelime=input("Kelimeyi gir")
    ilk=kelime[int(sayı[0])]
    iki=kelime[int(sayı[1])]
    if ilk == "s":
        print(kelime+kelime)
    elif iki=="t":
        print("lt"+kelime)
    elif iki=="l":
        print(kelime+"tl") 
    else:
        print(kelime[-1]+kelime)
