def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1988, 2008, 2016, 1987]
test_results = [True, True, True, False]

for i in range(len(test_data)):
    yil = test_data[i]

    print(yil, "->", end=" ")

    sonuc = is_year_leap(yil)

    if sonuc == test_results[i]:
        print("Doğru")
    else:
        print("Yanlış")
