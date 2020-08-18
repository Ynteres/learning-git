print("3. Zadanie 1")
order_list = {
    "Piekarnia": ["Chleb","Bulki","Paczek"],
    "Warzywniak": ["Marchew","Seler","Rukola"]
}
a=len(order_list)
print("Lista zakupów")
for sklep, produkty in order_list.items():
      print("Ide do %s, kupuję tu nstępujące rzeczy : %s" % (sklep.upper(), produkty))
print("W sumie kupuje w %d sklepach aż XX produktów." % (a))
print("%s" % (20*"==") )

""" MOD3 - ZADANIE 2 
Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
W następnym wierszu wyświetli te liczby podniesione do potęgi 3."""

print("3. Zadanie2")
nper5 = []
thirdpower = []
for n in range (0,101):
    if n %5 == 0 and n != 0:
        nper5.append(n)
print(nper5)
print("%s" % (20*"- -") )
for number in nper5:
    thirdpower.append(number **3)
print(f"liczby podniesione do potęgi 3 to {thirdpower} ")

print("GIT test 3")
