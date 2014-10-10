def count_words(arr):
    result = {}
    for i in arr:
        if i in result:
            result[i] += 1
        else:
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
    # n e ot 1 do len(word) / 2 :D:D
    pass
