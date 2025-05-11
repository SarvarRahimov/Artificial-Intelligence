# 1) İstifadəçidən iki rəqəm və bir əməliyyat (toplama, çıxma, vurma, bölmə) daxil etməsini tələb edən funksiya yazın. Mümkün xətaları (ValueError, TypeError və s.) idarə edin və müvafiq mesajlar çıxarın. Sonda da "Hesablama bitdi" mesajı çap olunsun.
def hesapla():
    try:
        a = float(input("Birinci ədədi daxil edin: "))
        b = float(input("İkinci ədədi daxil edin: "))
        operation = input("Hesablama əməliyyatını daxil edin (+, -, *, /): ")

        if operation == '+':
            print("Nəticə:", a + b)
        elif operation == '-':
            print("Nəticə:", a - b)
        elif operation == '*':
            print("Nəticə:", a * b)
        elif operation == '/':
            if b == 0:
                print("Sıfıra bölmək olmaz!")
            else:
                print("Nəticə:", a / b)
        else:
            print("Yanlış əməliyyat daxil edildi!")
    except ValueError:
        print("Rəqəm daxil edilməlidir!")
    except TypeError:
        print("Yanlış tip daxil edildi!")
    finally:
        print("Hesablama bitdi")

# 2) 1-dən 50-yə qədər olan rəqəmlərdən yalnız 11ə qalıqsız bölünənlərini list olaraq qaytarın.
result = [i for i in range(1, 51) if i % 11 == 0]
print(result)  # [11, 22, 33, 44]

# 3) Verilmiş sözlər siyahısından (["kitab", "qələm", "defter", "silgi"]) hər sözün ilk hərfini list olaraq qaytarın.
words = ["kitab", "qələm", "defter", "silgi"]
first_letters = [word[0] for word in words]
print(first_letters)  # ['k', 'q', 'd', 's']

# 4) Şəhər adları (["Bakı", "Gəncə", "Sumqayıt"]) və kodları ([12, 22, 18]) siyahılarından {şəhər: kod} dictionary olaraq qaytarın.
cities = ["Bakı", "Gəncə", "Sumqayıt"]
codes = [12, 22, 18]
city_dict = dict(zip(cities, codes))
print(city_dict)  

#5) Kilometri milə çevirən (mil = km * 0.621371) lambda funksiyası yazın və 5 fərqli dəyər üçün yoxlayın.
km_to_mile = lambda km: km * 0.621371
test_values = [1, 5, 10, 42, 100]
converted = list(map(km_to_mile, test_values))
print(converted)

#6) [100, 200, 300, 400] qiymətlərinə 18% vergi əlavə etmək üçün map() və lambda istifadə edin.
prices = [100, 200, 300, 400]
with_tax = list(map(lambda x: x * 1.18, prices))
print(with_tax)

# 7) [3, 7, 12] və [2, 4, 6] siyahılarının elementlərini ikiqat artırmaq və sonra cəmləmək üçün map() istifadə edin.
list1 = [3, 7, 12]
list2 = [2, 4, 6]
result = list(map(lambda x, y: (x*2) + (y*2), list1, list2))
print(result)  # [10, 22, 36]

# 8) [150, 80, 220, 45] siyahısından ən kiçik qiyməti reduce() ilə tapın.
from functools import reduce

numbers = [150, 80, 220, 45]
smallest = reduce(lambda x, y: x if x < y else y, numbers)
print(smallest)  # 45



