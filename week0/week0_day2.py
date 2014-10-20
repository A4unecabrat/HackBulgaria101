

def count_words(arr):
    result = {}
    for i in arr:
        if i in result:
            result[i] += 1
        elif i not in result and i.isalpha():
            result[i] = 1
    return result


def unique_words_count(arr):
    return len(count_words(arr))


def groupby(func, seq):
    result = {}
    for i in seq:
        if func(i) in result:
            result[func(i)].append(i)
        else:
            result[func(i)] = [i]
    return result


def prepare_meal(number):
    if number < 0:
        return False
    elif number == 0:
        return ""
    result = ""
    dev = 3
    while (dev < number):
        if number % dev == 0:
            result = result + "spam "
        dev = dev * 3
    if number % 5 == 0 and not result:
        result = result + "eggs"
    elif number % 5 == 0:
        result = result + "and eggs"
    return result


def reduce_file_path(path):
    result = ["/"]
    a = path.replace("/", " ").split()
    a.reverse()
    for i in range(0, len(a)):
        if a[i] != "." and a[i] != ".." and a[i - 1] != "..":
            result.insert(1, "/" + a[i])
    return "".join(result)[:1] + "".join(result)[2:]


def is_an_bn(word):
    pass


def simplify_fraction(fraction):
    a = [fraction[0], fraction[1]]
    if a[0] < a[1]:
        for i in range(2, a[1]):
            while(a[0] % i == 0 and a[1] % i == 0):
                a[0] = a[0] / i
                a[1] = a[1] / i
    else:
        for i in range(2, a[0]):
            while(a[0] % i == 0 and a[1] % i == 0):
                a[0] = a[0] / i
                a[1] = a[1] / i
    return tuple(a)


def sort_fractions(fractions):
    return (sorted(fractions, key=lambda x: float(x[0]) / float(x[1])))


def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        return nth_fib_lists(listA, listB, n - 2) + nth_fib_lists(listA, listB, n - 1)

#print(nth_fib_lists([], [], 100))
