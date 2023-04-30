def silnia(a):
    if a == 0:
        return 1
    else:
        return silnia(a-1)*a

def silnia_suma(b):
    suma = 0
    liczba = str(b)
    for x in range(0, len(liczba)):
        suma += silnia(int(liczba[x]))
    if suma == b:
        return True
    return False
def nwd(a, b):
    if b > a:
        return nwd(b, a)
    if a%b == 0:
        return b
    x = 2
    t = []
    while x<a and x<b:
        if a%x == 0 and b%x == 0:
            t.append(x)
            a = a/x
            b = b/x
        else:
            x += 1
    odp = 1
    for x in range(len(t)):
        odp *= t[x]
    return odp
print(nwd(40,10))
f = open('liczby.txt', 'r')
x = 1
p = []
odp_2 = []
while x < 100000:
    p.append(x)
    x = x*3
ile_1 = 0
for linia in f:
    x = int(linia.strip())
    if x in p:
        ile_1 += 1
    if silnia_suma(x):
        odp_2.append(str(x))
f.close()



print(f"4.1: {ile_1}")
print(f"4.2: {' '.join(odp_2)}")

f = open('liczby.txt', 'r')



najw_ciag = []
t = []
for linia in f:
    x = int(linia.strip())
    t.append(x)
for x in range(1, len(t)):
    if x == 1:
        nwd_3 = nwd(t[x], t[x-1])
        ciag = [t[x-1], t[x]]
    else:
        if nwd(nwd_3, t[x]) == 1:
            ciag = []
        if len(ciag) == 0 and nwd(t[x-1], t[x]) > 1:
            nwd_3 = nwd(t[x-1], t[x])
            ciag = [t[x-1], t[x]]
        elif nwd(t[x], nwd_3) > 1:
            ciag.append(t[x])
            nwd_3 = nwd(t[x], nwd_3)
        if len(ciag) > len(najw_ciag):
            najw_ciag = ciag
najw_dziel = nwd(najw_ciag[0], najw_ciag[1])

for x in range(2, len(najw_ciag)):
    najw_dziel = nwd(najw_dziel, najw_ciag[x])
print(f"4.3:")
print(f"pierwsza liczba ciągu: {najw_ciag[0]}")
print(f"długość ciągu: {len(najw_ciag)}")
print(f"najwiekszy wspolny dzielnik: {najw_dziel}")