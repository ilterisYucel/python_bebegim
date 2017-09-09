sayi_listesi = [5, 8, 4, 96, 2]
sonuc = sayi_listesi[0]
for sayi in sayi_listesi[1:]:
    if sayi > sonuc:
        sonuc = sayi
    else:
        continue
print(sonuc)

