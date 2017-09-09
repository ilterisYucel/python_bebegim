
#1'den 5'e kadar olan sayıların karesini ve küpünü
#içeren 2 boyutlu bir liste üreten aşağıdaki fonksiyonu
#tamamlayınız.(bir satır 'sayı, karesi, küpü' şeklindedir.)
iki_boyut_liste = []
for i in range(1, 6):
    satir = [i, i**2, i**3]
    iki_boyut_liste.append(satir)
print(iki_boyut_liste)