liste = [1,2,3,4,5]
print(liste)
print(liste[4])
print(type(liste))
liste [4] = 35
print(liste)

alt_liste = liste [2:4]
print(alt_liste)

tuple
tuple = (10,20,30)
print(tuple)
print(tuple[1])

tuble[1]=50
print(tuple)
alt_tuple = [1:4]
print(alt_tuple)

kumeler
kume={100,200,300,400,500}
print(kume)
kume.add(700)
print(kume)
kume.update([400,900])
print(kume)

dict dictionary sozluk

dict = {'anahtar1':'deger1','anahtar2':'deger2'}
print(dict)
deger = dict['anahtar1']
print(deger)

kume_list=list(kume)
print(kume_list)
print(type(kume_list))

kume_tuple=tuple(kume)
print(kume_tuple)
print(type(kume_tuple))

dict_list=list(dict.keys())
print(dict_list)
print(type(dict_list))

dict_list=list(dict.values())
print(dict_list)
print(type(dict_list))

sayilar=[10,8,5,3,15,10]
en_buyuk=max(sayilar)
en_kucuk=min(sayilar)
print(en_buyuk)
print(en_kucuk)
sayilar.append(20)
sayilar.append(1)
yeni_en_buyuk=max(sayilar)
yeni_en_kucuk=min(sayilar)
print(yeni_en_kucuk)
print(yeni_en_buyuk)
print(sayilar)

sayilar.pop()
print(sayilar)

sayilar.sort()
print(sayilar)

sayilar.reverse()
print(sayilar)

print(sayilar.count(10))

aralik = range(1,100)
print(list(aralik))

import random

rastgele_sayi = random.randint(1,100)
print("tutulan sayi",rastgele_sayi)








