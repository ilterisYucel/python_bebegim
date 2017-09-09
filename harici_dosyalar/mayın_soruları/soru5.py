
#5 ve 7 sayısının faktöriyel değerini
#bulan ve yazdıran aşağıdaki programı tamamlayınız.
def faktoriyel_bul(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi * faktoriyel_bul(sayi - 1)
print("{} in faktöriyeli {}".format(5, faktoriyel_bul(5)))
print("{} in faktöriyeli {}".format(7, faktoriyel_bul(7)))