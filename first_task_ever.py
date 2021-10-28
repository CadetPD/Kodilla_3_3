intro = "LISTA ZAKUPÓW"

weight1 = "1 kg sera"
weight2 = "1 kg"

currency = 'zł'

name1 = 'Roquefort'
name2 = 'Stilton' 
name3 = 'Brie'
name4 = 'Gouda'
name5 = 'Edam'
name6 = 'Parmezan'
name7 = 'Mozzarella'
name8 = "Czechosłowackiego sera z owczego mleka"

price1 = "{:.2f}" .format(12.50)
price2 = "{:.2f}" .format(11.24) 
price3 = "{:.2f}" .format(9.30)
price4 = "{:.2f}" .format(8.55)
price5 = "{:.2f}" .format(11) 
price6 = "{:.2f}" .format(16.50)
price7 = "{:.2f}" .format(14)
price8 = "{:.2f}" .format(122.32)

cheese_price1 = "%s %s za %s %s" % (weight1, name1, price1, currency)
cheese_price2 = "%s %s za %s %s" % (weight1, name2, price2, currency)
cheese_price3 = "%s %s za %s %s" % (weight1, name3, price3, currency)
cheese_price4 = "%s %s za %s %s" % (weight1, name4, price4, currency)

cheese_price5 = f"{weight1} {name5} za {price5} {currency}"
cheese_price6 = f"{weight1} {name6} za {price6} {currency}"

cheese_price7 = "{} {} za {} {}".format(weight1, name7, price7, currency)
cheese_price8 = "{} {} za {} {}".format(weight2, name8, price8, currency)

print(intro)
print(cheese_price1)
print(cheese_price2)
print(cheese_price3)
print(cheese_price4)
print(cheese_price5)
print(cheese_price6)
print(cheese_price7)
print(cheese_price8)
print('SMACZNEGO!')

""""
Witam,
eksperymentowałem z kilkoma formatowaniami żeby nie robić trzech różnych list. Mam nadzieję, że to nie jest jakiś wielki grzech ;)

Próbowałem użyć formatera %d do zmiennej 'price' ale zwraca tylko liczby całkowite. Dla formatera %s i w linijkach napisanych wg P3.6 (jak w Module) i z użyciem funkcji z yt zwraca tylko pierwsze zero po przecinku lub ostatnią cyfrę poprzedzającą zero. Skoro format ceny miał być polski to dopisałem im te zera ale mam w związku z tym mam pytanie: w jaki sposób można zwrócić całą wartość dla wszystkich zmiennych 'price', tj. do dwóch miejsc po przecinku bez sztukowania?

Z góry dzięki za odpowiedź i czekam na krytyczne uwagi :)

Pozdrawiam serdecznie,
PD
"""
