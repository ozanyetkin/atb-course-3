#Fibonacci serisi 0 ve 1 le başlar.
#Sonraki sayılar kendilerinden önce gelen 2 sayının toplamıdırlar.
#Bu seriyi 50'inci sayıya kadar ilerletiniz.
fibo=[0,1]
for i in range(48):
    fibo.append(fibo[i]+fibo[i+1])
print(fibo)
