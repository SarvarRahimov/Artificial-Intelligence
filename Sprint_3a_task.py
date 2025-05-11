# 1) x dəyişəni verilmişdir. Əgər x > 0 olarsa "müsbət", x < 0 olarsa "mənfi", bərabərdirsə "sıfır" çap etsin.
x = int(input("x daxil edin: "))
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

# 2) n rəqəmi cütdürsə "cüt", təkdirsə "tək" çap etsin.
n = int(input("n daxil edin: "))
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

#3) a, b, c rəqəmləri verilmişdir. Ən böyük rəqəmi çap etsin.
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("Ən böyük:", max(a, b, c))

# 4) day dəyişəni 1-7 arası rəqəmdir. Müvafiq həftə gününü (1 = "Bazar ertəsi", ..., 7 = "Bazar") çap etsin, əks halda "Yanlış gün" yazsın.
day = int(input("Gün nömrəsi daxil edin (1-7): "))
days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(days.get(day, "Yanlış gün"))

#5) temp dəyişəni temperaturdur. Əgər temp < 0 olarsa "soyuq", 0-20 arası olarsa "normal", 20-dən böyükdürsə "isti" çap etsin.
temp = float(input("Temperaturu daxil edin: "))
if temp < 0:
    print("soyuq")
elif temp <= 20:
    print("normal")
else:
    print("isti")

#6) password adlı string verilmişdir. Əgər uzunluğu 8-dən kiçikdirsə "qısa", 8-12 arasıdırsa "orta", 12-dən böyükdürsə "uzun" çap etsin.
password = input("Şifrə daxil edin: ")
length = len(password)
if length < 8:
    print("qısa")
elif length <= 12:
    print("orta")
else:
    print("uzun")

#7) x rəqəmi həm 3-ə, həm də 5-ə bölünürsə "3 və 5", yalnız 3-ə bölünürsə "3", yalnız 5-ə bölünürsə "5", heç birinə bölünmürsə "heç biri" çap etsin.
x = int(input("x daxil edin: "))
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

# 8) 0-dan 20-yə qədər cüt rəqəmləri çap etsin.
for i in range(0, 21, 2):
    print(i)

# 9) "Bağda ərik var idi …" stringinin hər elementini for ilə ayrı-ayrılıqda çap edin.
text = "Bağda ərik var idi …"
for char in text:
    print(char)

# 10) 1-dən 10-a qədər rəqəmləri çap edin, amma 3 xaric.
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# 11) 1-dən başlayaraq ilk 5-ə bölünən rəqəmi tapın və while ilə çap edin (break istifadə edin).
i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1

# 12) (1, 3, 5, 7, 9) listində/vectorunda 5-i tapın və indeksini çap edin (break istifadə edin).
nums = (1, 3, 5, 7, 9)
for index, value in enumerate(nums):
    if value == 5:
        print("İndeks:", index)
        break
