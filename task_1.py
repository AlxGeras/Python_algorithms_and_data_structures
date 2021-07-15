def count_subs(string):
    result = set()

    for i in range(1, len(string)):
        for j in range(len(string) - i + 1):
            h = hash(string[j:i+j])
            result.add(h)
    return len(result)


s2 = input('Введите строку: ')
print(f'В данной строке {count_subs(s2)} различных подстрок')