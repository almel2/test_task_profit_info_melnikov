list2 = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

list1 = [
    ['False', 'True'],
    0,
    ['first', 'second', 'third']
]


def validator_lists(lists):
    for i in range(len(lists)):
        if not isinstance(lists[i], list):
            lists[i] = [lists[i]]
    return lists


def findvariant(lists, variant):
    lists = validator_lists(lists)
    result = []
    counter = 1

    last_value_index = variant % len(lists[-1]) - 1
    result.append(lists[-1][last_value_index])

    counter *= len(lists[-1])

    for list in lists[::-1][1:]:
        index = variant // counter % len(list)
        result.append(list[index])
        counter *= len(list)

    print(result[::-1])


findvariant(list1, 4)
findvariant(list2, 1)
findvariant(list2, 138)
findvariant(list2, 1012)
