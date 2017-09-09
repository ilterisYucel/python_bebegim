
#[[12, 15, 27],
# [20, 22, 45],
# [8, 10, 97]] 2 boyutlu listesinden 5'e
#tam bölünebilen sayıları bulup yazdıran aşağıdaki
#programı tamamlayınız.
liste = [[12, 15, 27]
         [20, 22, 45]
         [8, 10, 97]]
for satir in liste:
    for sayi in satir:
        if sayi % 5 == 0:
            print("{} sayisi 5 ile bölünür.".format(sayi))