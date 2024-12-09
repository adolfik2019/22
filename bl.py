# task 1
# n = 5
# total = 0
# for i in range(1, n):
#     total += i

# print(total)


# task 2
# input_numbers = input("Введите числа")

# numbers = []

# for num in input_numbers.split(","):
#     numbers.append(int(num))

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Четные ", even)
# print("Нечетные ", odd)


# task 3
# n = int(input("Введите число"))

# factorial = 1

# for i in range(1, n):
#     factorial *= i

# print(factorial)


# task 4
# input_numbers = input("Введите числа")

# numbers = []

# for num in input_numbers.split(","):
#     numbers.append(int(num))

# max_num = numbers[0]
# min_num = numbers[0]

# for num in numbers:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print(f"Max: {max_num}, Min: {min_num}")


# task 5
# n = input("Введите число ")

# sum_of_digits = 0

# for digit in n:
#     sum_of_digits += int(digit)

# print(sum_of_digits)


# task 6
# input_numbers = input("Введите числа")

# numbers = []

# for num in input_numbers.split(","):
#     numbers.append(int(num))

# count_dict = {}

# for num in numbers:
#     count_dict[num] = count_dict.get(num, 0) + 1

# for key, value in count_dict.items():
#     print(f"{key}: {value}")


# task 7
# input_numbers = input("Введите числа ")

# numbers = []

# for num in input_numbers.split(","):
#     numbers.append(int(num))

# updated_list = []

# for num in numbers:
#     if num % 2 != 0:
#         updated_list.append(num)

# print(updated_list)


# task 8
# input_words = input("Введите слова")

# words = []

# for word in input_words.split(","):
#     words.append(word)

# min_length = int(input("минимальная длина строки "))

# filtered_words = []

# for word in words:
#     if len(word) > min_length:
#         filtered_words.append(word)

# print("Список с длиной больше", min_length, ":", filtered_words)


# task 9
# input_numbers = input("Введите числа")

# numbers = []

# for num in input_numbers.split(","):
#     numbers.append(int(num))

# positives = []
# negatives = []

# for num in numbers:
#     if num > 0:
#         positives.append(num)
#     elif num < 0:
#         negatives.append(num)

# print("Положительные", positives)
# print("Отрицательные", negatives)


# task 10
# input_words = input("Введите слова")

# words = []

# for word in input_words.split(","):
#     words.append(word)

# n = int(input("Введите n"))

# count = 0

# for word in words:
#     if len(word) > n:
#         count += 1

# print("Кол-во слов с длиной больше", n, ":", count)


# task 11
input_phrases = input("Введите слова")

phrases = []

for phrase in input_phrases.split(","):
    phrases.append(phrase)

contains_digits = []

for phrase in phrases:
    for char in phrase:
        if char.isdigit():
            contains_digits.append(phrase)
            break

print(contains_digits)
