
#a ve b şeklinde  6 ve 19 olarak belirlenmiş
#değişkenlerin tek mi çift mi olduğunu bulan
#ve yazdıran aşağıdaki programı tamamlayınız.
def tek_cift(sayi):
    if sayi % 2 == 0:
        return "çift"
    else:
        return "tek"
a = 6
b = 19
print("{} sayısı {}tir.".format(a, tek_cift(a)))
print("{} sayısı {}tir.".format(b, tek_cift(b)))