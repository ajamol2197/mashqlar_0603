# 1
def son(a, b, c):
    if a > 0 and b > 0 and c >0:
        return "hammasi musbat"

    return "manfiy mavjud"


y = son(12, 9, 7)
print(y)

# 2
def son(a):
    if 1 <= a < 9:
        return "bir honali"
    elif 10 <= a < 99:
        return "ikki honali"

    return "boshqa"


y = son(34)
print(y)

# 3
def son(a, b):
    if a == 1 and b == 2:
        return "Turli turdagi"

    return "bir hil turdagi"


y = son(12, 10)
print(y)

# 4
def matn(a):
    if len(a > 6):
        return "mos keladi"

    return "mos emas"


y = matn("Turli turdagi")
print(y)

# 5
def yosh(a):
    if a < 18:
        return "voyaga yetmagan"
    elif a >= 18:
        return "talaba"
    else:
        return "oddiy fuqaro"


o = int(input("yosh klirit: "))
print(yosh(o))

# 6
def son(a):
    if a / 3 and a / 5:
        return "mos"
    else:
        return "mos emas"


y = son(19)
print(y)

# 7
def log(a):
    if len(a) < 5 or " " in a:
        return "notogri login"
    else:
        return "togri login"


y = log("igvdce")
print(y)

# 8
def parol(a):
    katta = False
    raqam = False

    for belgi in a:
        if belgi.isupper():
            katta = True
        if belgi.isdigit():
            raqam = True

    if katta and raqam:
        return "Kuchli parol"
    else:
        return "Kuchsiz parol"


p = input("Parol kiriting: ")
print(parol(p))

# 9
def son(a):
    if a >= 2:
        return "musbat juft"
    elif a >= 1:
        return "musbat toq"
    else:
        return "manfiy yoki nol"


y = son(8)
print(y)

# 10
def matn(a, b):
    if len(a) == len(b):
        return "Uzunligi teng"
    else:
        return "uzunligi teng emas"


y = matn("3434", "545j4")
print(y)

# 11
def matn(a):
    if a[0].isupper and a[-1] == ".":
        return "togri gap"

    return "xato farmat"


y = matn("=Ali.")
print(y)


# 12
def emil(a):
    if a == "@" and a == ".":
        return "Email to‘g‘ri"

    return "Email noto‘g‘ri"


y = emil("asdjb.com")
print(y)

# 13
def ism(a):
    if a < 3:
        return "juda qisqa"
    elif 3 < a < 10:
        return "normal"

    return "juda uzun"


y = ism(12)
print(y)

# 14
def son(a):
    if a >= 100 and a >= 2:
        return "katta juft"

    return "shartga mos emas"


y = son(104)
print(y)

# 15
def matn(a):
    for belgi in a:
        if not (a.isalpha() or belgi == " "):
            return "ortiqcha belgilar bor"
    return "toza matn"


y = matn("ddf bdytr ")
print(y)

# 16
def son(a, b):
    if a >= 2 and b >= 2:
        return "ikkalasi juft"
    elif a >= 1 and b >= 1:
        return "ikkalasi toq"

    return "aralash"


y = son(4, 8)
print(y)

# 17
def raqam(a):
    if len(a) == 9:
        return "togri raqam"

    return "notogri raqam"


y = raqam("889877673")
print(y)

# 18
def matn(a):
    if a[::-1] and len(a) > 5:
        return "Katta palindrom"

    return "oddiy yoki pilidrom emas"


y = matn("aziza")
print(y)

# 19
def son(a):
    if 0 < a < 50:
        return "kichik musbat"
    elif a > 50:
        return "katta musbat"

    return "manfiy yoki nol"


y = son(43)
print(y)

# 20
def nomi(a, b):
    if len(a) >= 6 and len(b) >= 6:
        return "qabul qilindi"

    return "Ma'lumotlar juda qisqa"


y = nomi("binish8", "12541362")
print(y)

# 21
def son(a, b, c):
    natija = max(a, b, c)
    return natija


y = son(23, 45, 32)
print(f"eng katta {y}")

# 22
def oy(a):
    if a == 3 and a == 4 and a == 5:
        return "bahor"
    elif a == 6 and a == 7 and a == 8:
        return "yoz"
    elif a == 9 and a == 10 and a == 11:
        return "kuz"
    elif a == 12 and a == 1 and a == 2:
        return "qish"

    return "notopgri oy"


y = oy(15)
print(y)

# 23
def son(a):
    if a % == 2 and a % == 3:
        return "6 ga karrali"
    elif a % == 2 and a % == 3:
        return "qisman mos"

    return "mos emas"


y = son(7)
print(y)

# 25
def son(a, b):
    if a - b > 10:
        return "ancha katta"

    return "farq kichik"


y = son(100, 10)
print(y)

# 26
def parol(a):
    if len(a) < 6:
        return "juda zaif"
    elif len(a) < 10:
        return "ortacha"

    return "kuchli"


y = parol("1243")
print(y)

# 27
def harf(a):
    if a.isupper():
        return "unli"
    elif a.islower():
        return "undosh"

    return "harf emas"


y = harf("ytu")
print(y)

# 28
def matn(a):
    if a[0] == " " and a[-1] == " ":
        return "Keraksiz bo‘sh joy bor"

    return "toza matn"


y = matn(" kam  ")
print(y)

# 29
def tekshir(a, b):
    if a == 0 or b == 0:
        return "Nol mavjud"
    elif a > 0 and b > 0:
        return "Ikkalasi musbat"
    else:
        return "Boshqa holat"


a = int(input("sonni kiriting: "))
b = int(input("sonni kiriting: "))
print(tekshir(a, b))

# 30
def son(n):
    if 1 <= n <= 100:
        if n % 2 == 0:
            return "Mos juft"
        else:
            return "Mos toq"
    else:
        return "Oraliqdan tashqarida"


n = int(input("Son kiriting: "))
print(son(n))
