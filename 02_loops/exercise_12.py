# Bir tam sayı listesi verilmiş olsun. x değerinin bu listeye göre mean squared errorunu bulmak istiyoruz.
#Mean Squared Error = https://en.wikipedia.org/wiki/Mean_squared_error
import random
listem=random.sample(range(0, 1000), 100)
x=float(input("x değerini veriniz"))
toplam=0
for i in listem:
    toplam+=(x-i)**2
print(toplam/len(listem))
