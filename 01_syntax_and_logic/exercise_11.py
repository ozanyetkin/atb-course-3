#Kullanıcıdan kök isteyin, a ve b olsun.
#(x-a)(x-b)'u x^2-(a+b)x+ab=0 olarak yazın.
sayılar=input("İstediğiniz denklem için kökleri verin.").split(",")
a=int(sayılar[0])
b=int(sayılar[1])
beta=-1*(a+b)
sabit=a*b
print(f"Denkleminiz: x\u00b2+{beta}x+{sabit}=0")
