# Terminalde sorun hey Bob ne yiyelim. Eğer kebap derse boşver pizza
#  daha iyi pizza yiyelim diyin.Eğer pizza derse kebap ikiside değilse
# ben sadece kebap veya pizza yerim diyin.
teklif=input("Hey Bob ne yiyelim?")
if teklif=="kebap":
    print("Boşver kebabı. Pizza daha iyi, pizza yiyelim.")
elif teklif=="pizza":
    print("Boşver pizzayı. Kebap daha iyi, kebap yiyelim.")
else:
    print("Ben sadece kebap yada pizza yerim.")

# not (teklif=="kebap" or teklif=="pizza") buda kullanılabilir.