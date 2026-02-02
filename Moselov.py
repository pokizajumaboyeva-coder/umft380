def funkMoselov(a, b, c):
    sonlar = [a, b, c]
    sonlar.sort(reverse=True)
    return sonlar[0] + sonlar[1]


print(funkMoselov(4, 7, 3))  # 11
print(funkMoselov(3, 1, 5))  # 8
