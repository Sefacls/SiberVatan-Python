import re
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception("parola en az 8 karakter")
    elif not re.search("[a-z]",parola):
        raise Exception("parola küçük haf içercek")
    elif not re.search("[A-Z]",parola):
        raise Exception("parola buyuk harf içercek")
    elif not re.search("[!,^,+,#,!,<,>,=,?,_,%,£,$,½,&,*,-,|]",parola):
        raise Exception("özel karakter içermeli")



password="123456789Ss#"
try:
    parola_kontrol(password)
except Exception as ex:
    print(ex)
else:
    print("parola basarili")
