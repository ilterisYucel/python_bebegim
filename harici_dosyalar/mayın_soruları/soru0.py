
#Üç kenarı a,b,c değişkenleriyle
#5,6,7 olarak verilmiş bir üçgenin
#alanını hesaplayan aşağıdaki programı tamamlayınız.
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Üçgenin alanı {}.".format(area))