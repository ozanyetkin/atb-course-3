#Kullanıcıdan pozitif tam sayı al.
#Rakamlarının toplamını, çarpımını ve sayının kendisini büyüklük olarak sıralayın. Sayıların kendisine gerek yok...
#https://codeshare.io/WdwxWy
"""
sayı=input("Sayı giriniz")
toplam=0
çarpım=1
if 0<=int(sayı)<=9:
    print("sayı=toplam=çarpım")
else:
    for rakam in sayı:
        if int(rakam)==0:
            print("sayı>toplam>çarpım")
            break
        toplam+=int(rakam)
        çarpım*=int(rakam)
    if toplam>çarpım:
        print("sayı>toplam>çarpım")
    elif toplam==çarpım:
        print("sayı>toplam=çarpım")
    else:
        print("sayı>çarpım>toplam")
    """
sayı=input("Sayı giriniz")
toplam=0
çarpım=1
if 0<=int(sayı)<=9:
    print("sayı=toplam=çarpım")
else:
    flag=True
    for rakam in sayı:
        if int(rakam)==0:
            flag=False
            print("sayı>toplam>çarpım")
            break
        toplam+=int(rakam)
        çarpım*=int(rakam)
    if flag:
        if toplam>çarpım:
            print("sayı>toplam>çarpım")
        elif toplam==çarpım:
            print("sayı>toplam=çarpım")
        else:
            print("sayı>çarpım>toplam")
    
    
    