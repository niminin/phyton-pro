import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("kaç karakter olsun cnm"))

parola = ""
for i in range(uzunluk):
    parola += random.choice(karakterler)


print(parola)