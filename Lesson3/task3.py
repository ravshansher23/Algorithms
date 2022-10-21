str_line = str(input("Введите строку: "))

test_set = set()
test_dict = {}
for i in range(len(str_line)):
    for j in range(len(str_line) - 1 if i == 0 else len(str_line), i, -1):
        test_set.add(hash(str_line[i:j]))
        print(str_line[i:j], i, j)
        test_dict[str_line[i:j]] = hash(str_line[i:j])

print(len(list(test_dict.keys())), list(test_dict.keys()))
print("Количество различных подстрок в этой строке:", len(test_set))