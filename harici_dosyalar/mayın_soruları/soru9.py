
#6. ve 10. sıradaki fibonacci sayılarını bulan
#ve bu sayıları yazdıran aşağıdaki programı tamamlayınız.
def fibonacci_bul(sayi_sirasi):
    if sayi_sirasi < 2:
        return 1
    return fibonacci_bul(sayi_sirasi-1) + fibonacci_bul(sayi_sirasi-2)
print("{}. sıradaki fibonacci sayısı {}.".format(6, fibonacci_bul(6)))
print("{}. sıradaki fibonacci sayısı {}.".format(10, fibonacci_bul(10)))
