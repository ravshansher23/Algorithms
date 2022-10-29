from collections import Counter, deque


def haffman_tree(s):
    count_s = Counter(s)
    sort_counter = deque(sorted(count_s.items(), key=lambda item: item[1]))

    if len(sort_counter) != 1:
        while len(sort_counter) > 1:
            weight = sort_counter[0][1] + sort_counter[1][1]

            new_elem = {0: sort_counter.popleft()[0], 1: sort_counter.popleft()[0]}
            print(new_elem)
            for i, j in enumerate(sort_counter):
                if weight > j[1]:
                    continue
                else:
                    sort_counter.insert(i, (new_elem, weight))
                    break
            else:
                sort_counter.append((new_elem, weight))
        else:
            weight = sort_counter[0][1]
            new_elem = {0: sort_counter.popleft()[0], 1: None}
            sort_counter.append((new_elem, weight))
        return sort_counter[0][0]

code_table = dict()

def code_haff(tree, name=''):
    if not isinstance(tree, dict):
        code_table[tree] = name

    else:
        code_haff(tree[0], name=f'{name}0')
        code_haff(tree[1], name=f'{name}1')
s = "beep boop beer!"

code_haff(haffman_tree(s))
print(code_table)
for i in s:
    print(code_table[i], end=' ')
