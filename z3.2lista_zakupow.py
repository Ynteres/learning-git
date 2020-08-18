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


