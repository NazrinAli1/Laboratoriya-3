from random import randint

n = 24
a = [[0] * n for _ in range(n)]  # 0'larla dolu bir n x n matris yaradırıq (yaradılmışdır).

# Matrisi təsadüfən ədədlərlə doldururuq
for i in range(n):
    for j in range(n):
        a[i][j] = randint(-12, 24)

print(a)

# Baş çarpazda təkrarlanan müsbət dəyərlərin ədədi ortasını hesablayırıq və yerinə qoyuruq
for i in range(n):
    positive_numbers = [num for num in a[i] if num > 0]  # Müsbət ədədləri seçib
    if len(positive_numbers) > 0:
        average = sum(positive_numbers) / len(positive_numbers)  # Sayıların Ədədi ortasını hesablayıb
        a[i][i] = average  # Baş diaqonalda ədədi ortanı  yerinə qoyuruq


# Matrisi yazdır deyib, çıxarırıq


print("Baş çaprazdaki ədədi ortalar əlavə edilmiş matris:")
for row in a:
    print(row)
