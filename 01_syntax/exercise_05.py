# Kullanıcıdan saniye bilgisi alın. Kaç gün,saat,dakika ve saniye bulup yazdırın.
zaman=int(input("Saniye bilgisi giriniz"))

dakika=zaman//60
saniye=zaman%60
saat=dakika//60
dakika=dakika%60
gün=saat//24
saat=saat%24

print(f"{gün} gün, {saat} saat, {dakika} dakika, {saniye} saniye")
# x=a/b y=int(x), z=(x-y)*b  yada y=a//b ve z=a%b