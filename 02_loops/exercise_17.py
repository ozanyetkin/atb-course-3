#Verilen tam sayıyı binary (ikilik sistemde) yazınız.
#  Binary yazımında her arka arkaya 1 dizisinden sonra aynı uzunlukta 0 dizisi geliyo mu
#  kontrol edip söyleyin.
"""
sayımız=int(input("Sayıyı giriniz: "))
i=0
bina=""
while sayımız!=0:
    i+=1
    if sayımız%(2**i)==0:
        bina="0"+bina
    else:
        bina="1"+bina
        sayımız-=2**(i-1)
print(bina)
"""
bina=input("bina girinbiz")
count=0
increment=1
flag=False
for i in range(len(bina)-1):
    count+=increment
    if increment==-1 and bina[i+1]=="1" and count!=0:
        flag=True
        break 
    if bina[i]!=bina[i+1]:
        increment*=-1
    
    if count<0:
        break
count+=increment
if flag:
    print(False)
else:
    if count==0:
        print(True)
    else:
        print(False)

    

    

