# a=90
# b="siber vatan"
# num1,num2,num3=5,55,555
# print("sayılar",num1,num2,num3)

# num1=num1+50
# num2=num2+55
# num3=num3+90

# num1+=50

# numbels=(50,55,66)
# print(type(numbels))
# num1,num2,num3,num4=numbels
# print(num3)


# a,b,c,d=50,100,50,75
# print(str(a < b))

# a,b,c,d=50,100,50,75

# sonuc=(a>b)
# print(int(sonuc))

# sonuc=(a==c)
# print(sonuc)

# sonuc=(a>b)
# print(sonuc)

# sonuc=(a!=b)
# print(sonuc)

# username1="ceku"
# username2="arif"

# print("a.r.o.g.'a hos geldin.\n")
# username_input=input("kullanıcı adı gir:")

# sonuc1 = (username1.lower()==username_input.lower())
# sonuc2 = (username2.lower()==username_input.lower())

# sonuc3=(sonuc1 != sonuc2)

# print("eşleşme sonucu...", sonuc3)

users=("sefa.gmail:123","ahmet.gmail:321")

input_mail=input("mail gir:")
input_sifre=input("sifre gir:")

sonuc_mail=(input_mail in users.keys()) 
sonuc_sifre=(input_sifre in users.values())

sonuc_final=(int(sonuc_mail==sonuc_sifre)==2)
print("eşleşme durumu...",sonuc_final)
