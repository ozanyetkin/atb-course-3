#Verilen tam sayıyı binary (ikilik sistemde) yazınız.
#  Binary yazımında her arka arkaya 1 dizisinden sonra aynı uzunlukta 0 dizisi geliyo mu
#  kontrol edip söyleyin.

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
"""
"""
bina=input("bina girinbiz")
count=1
for index in range(1,len(bina)):
    if bina[index]=="1":
        count+=1
    else:
        count-=1
    if bina[index-1]=="0" and bina[index]=="1":
        if count!=1:
            count=13
            break
if count!=0:
    print(False)
else:
    print(True)
    
"""

count=1
index=1
while not (index==len(bina) or (bina[index]=="1" and bina[index-1]=="0" and count!=0)):
    if bina[index]=="1":
        count+=1
    else:
        count-=1
    index+=1
if count==0:
    print(True)
else:
    print(False)


    

    

    

