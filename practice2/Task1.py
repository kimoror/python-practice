x2_2 = {'cuda': 2, 'eq': 1, 'dm': 0}
x3 = {'dm': 5, 'arc': 4, 'haxe': 3}
x4 = {'urweb': x3, 'gdb': x2_2}
x0 = {2001: 6, 2020: x4}
x2_1 = {'cuda': 9, 'eq': 8, 'dm': 7}
x1 = {'swift': 10, 'antlr': x2_1, 'asp': x0}


def level_two(plenty, subset):
    for el in plenty:
        for j in subset.keys():
            if j == el:
                if isinstance(subset.get(j), int):
                    return subset.get(j)
                else:
                    plenty.remove(el)
                    return level_two(plenty, subset.get(j))


def f21(plenty):
    return level_two(plenty, x1)


print(f21([2020, 'antlr', 'dm', 'arc', 'urweb']))
