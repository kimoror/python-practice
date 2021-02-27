x2_2 = {'cuda': 2, 'eq': 1, 'dm': 0}
x3 = {'haxe': 3, 'arc': 4, 'dm': 5}
x4 = {'urweb': x3, 'gdb': x2_2}
x0 = {2001: 6, 2020: x4}
x2_1 = {'cuda': 9, 'eq': 8, 'dm': 7}
x1 = {'swift': 10, 'antlr': x2_1, 'asp': x0}


def level_two(plenty, subset):
    for j in subset.keys():
        for el in plenty:
            if j == el:
                if isinstance(subset.get(j), int):
                    return subset.get(j)
                else:
                    plenty.remove(el)
                    return level_two(plenty, subset.get(j))


def f21(plenty):
    return level_two(plenty, x1)


print(f21([2020, 'asp', 'dm', 'dm', 'gdb']))
