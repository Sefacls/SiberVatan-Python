def emeklilik (yas):
    emeklilik=65
    if yas < emeklilik:
        kalan_yil = emeklilik - yas
        print(kalan_yil)
    else:
        print("emeklisin")
yas = int(input("Yaş Gir:"))
emeklilik(yas)






def asal_sayilari_bul(sayi1,sayi2):
    asal_sayila=[]
    for sayi in range (sayi1,sayi2 + 1):
        if sayi > 1:
            for i in range (2,sayi):
                if (sayi % i) == 0:
                    break
            else:
                asal_sayilar.append(sayi)
    return asal_sayilar
sayi1=int(input("sayi gir"))    
sayi2=int(input("sayi gir"))    
asal_sayilar = asal_sayilari_bul(sayi1, sayi2)
print(f"{sayi1} ile {sayi2} asal sayilar: {asal_sayilar}")



def en_buyuk sayi(list):
    en_buyuk = max(list)
    return en_buyuk

    
def en_kucuk sayi(list):
    en_kucuk = min(list)
    return en_kucuk

list1=[3,4,5,6,88,99]
list2=[1,23,4,5]

en_buyuk = en_buyuk_sayi(list)
en_kucuk = en_kucuk_sayi(list)

print({en_buyuk},{en_kucuk})





def sayi(list):
    if len(list) < 2:
        return False
    else:
        return list[0] == list[-1]
list=[3,4,5,6,7]
print(sayi(list))



def palindrome(sayi):
    sayi.str = str(sayi)
    ters_sayi_str = sayi_str[::-1]
    if sayi_str == ters_sayi_str:
        return True
    else:
        return False
sayi = int(input("sayi gir"))
if palindrome (sayi):
    print("palindrome")
else:
    print("palindrome deil")


import random
a=random.randrange(1,7)
while True:
  x=int(input("Bir sayı giriniz"))
  if x==a:
    print("öldün")
    break
  else:
   print("yaşadın!")


def sayilar():
        list1=[1,3,6,9,5,12,60]
        list2=[4,6,20,65,98,36,45]
        yenilist=[]
        
        for i in list1:
            if i%2==0:
                yenilist.insert(0,i)
        for a in list2:
            if a%2!=0:
                yenilist.insert(0,a)
        print("yenilist=",yenilist)
        
sayilar()














