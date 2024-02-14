def toplam (sayi1,sayi2):
   return sayi1+sayi2
def cikarma (sayi1,sayi2):
   return sayi1-sayi2
def carpma (sayi1,sayi2):
   return sayi1*sayi2
def bolme (sayi1,sayi2):
    if sayi2 == 0:
        print ("tanimsiz")
    else:
        return sayi1/sayi2
def faktöriyel (sayi1):
    if sayi1 == 0:
       return 1
    else:
        return sayi1 * faktöriyel(sayi1-1)
    

    devametsinmi = True
while (devametsinmi):
    print("toplama için 1")

    print("çikartma için 2")
    print("carpma için 3")
    print("bolme için 4")
    print("cikis için 5")
    print("faktöriyel için 6")
    secenek=input("seç")
    sayi1=int(input("sayi gir:"))
    sayi2=int(input("sayi gir:"))

    if (secenek==1):
         sonuc=toplam(sayi1,sayi2)
    elif (secenek==2):
        sonuc=cikarma(sayi1-sayi2)
    elif (seçenek==6):
        sanuc=faktöriyel(sayi1*(sayi1-1))
    elif (secenek==3):
        sonuc=carpma(sayi1*sayi2)
    elif (secenek==4):
        sonuc=bolme(sayi1/sayi2)
    elif(secenek==5):
        devametsinmi= False
    else:
        print("lütfen geçerli bir sayi gir:")
        continue
    print(sonuc)
