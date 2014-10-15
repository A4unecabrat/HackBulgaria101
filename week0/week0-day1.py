def nth_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n-2)


def sum_of_digits(n):
    total = 0
    while n != 0:
        total = total + n % 10
        n = n / 10
    return total


def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n/2+1):
        if n % i == 0:
            return False
    return True

def prime_number_of_divisors(n):
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter += 1
    return is_prime(counter)


def sevens_in_a_row(arr, n):
    count = 0
    while count != n:
        if arr == []:
            return False
        elif arr[0] == 7:
            count += 1
        elif count > 0:
            count -= 1
        arr.remove(arr[0])
    return True


def is_int_palindrome(n):
    lst = list(str(n))
    for i in range(0, len(lst)/2):
        if lst[i] != lst[-i-1]:
            return False
    return True


def contains_digit(number, digit):
    return str(digit) in list(str(number))


def contains_digits(number, digits):
    for i in range(0, len(digits)):
        if str(digits[0]) in list(str(number)):
            digits.remove(digits[0])
    return digits == []


def is_number_balanced(n):
    sum_left = 0
    sum_right = 0
    x = list(str(n))
    for i in range(0, len(x)/2):
        sum_left += int(x[i])
        sum_right += int(x[-i-1])
    return sum_right == sum_left


def count_substrings(haystack, needle):
    return haystack.count(needle)


def count_vowels(words):
    vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for i in words:
        if i.lower() in vowels:
            count += 1
    return count


def count_consonants(words):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    count = 0
    for i in words:
        if i.lower() in consonants:
            count += 1
    return count


def number_to_list(n):
    result = list(str(n))
    for i in range(0, len(result)):
        result[i] = int(result[i])
    return result


def list_to_number(digits):
    result = 0
    for i in range(0, len(digits)):

        result += digits[-i-1] * 10 ** i
    return result


def biggest_difference(arr):
    difference = 0
    for i in arr:
        for j in arr:
            if abs(i - j) > abs(difference):
                difference = i - j
    return difference


def is_increasing(seq):
    for i in range(1, len(seq)):
        if seq[i] <= seq[i-1]:
            return False
    return True


def is_decreasing(seq):
    for i in range(1, len(seq)):
        if seq[i] >= seq[i-1]:
            return False
    return True


def zero_incert(n):
    result = []
    digits = list(str(n))
    for i in range(0, len(digits)):
        if (digits[i] == digits[i - 1] or
           (int(digits[i])+int(digits[i - 1])) % 10 == 0)and i != 0:
            result.append('0')
            result.append(digits[i])
        else:
            result.append(digits[i])
    return int("".join(result))


def sum_matrix(m):
    total = 0
    for i in m:
        for j in i:
            total += j
    return total


def matix_bombing_plan(m):
    result = {}
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if (i == 0 or i == len(m) - 1) and (j == 0 or j == len(m[i]) - 1):
                result[(i, j)] = sum_matrix(m) - 3 * m[i][j]
            elif (i == 0 or i == len(m) - 1) and(j != 0 or j != len(m[i]) - 1):
                result[(i, j)] = sum_matrix(m) - 5 * m[i][j]
            elif (j == 0 or j == len(m[i]) - 1) and(i != 0 or i != len(m) - 1):
                result[(i, j)] = sum_matrix(m) - 5 * m[i][j]
            else:
                result[(i, j)] = sum_matrix(m) - 8 * m[i][j]
    return result


def next_hack(n):
    n += 1
    while not (is_int_palindrome(int(bin(n)[2:])) and
               bin(n).count("1")) % 2 != 0:
        n += 1
    return n


def nan_expand(times):
    if times == 0:
        return ""
    elif times == 1:
        return "Not a NaN"
    else:
        return "Not a " + nan_expand(times - 1)


def iterations_of_nan_expand(words):
    return words.count("Not a ")


def prime_factorization(n):
    result = []
    while n > 1:
        for i in range(2, n+1):
            if is_prime(i) is True:
                counter = 0
                while n % i == 0:
                    counter += 1
                    n = n / i
                if counter > 0:
                    result.append((i, counter))
    return result


def calculate_coins(value):
    result = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
    MONEH = [100, 50, 20, 10, 5, 2, 1]
    value = value * 100
    while value > 0:
        for i in MONEH:
            while value - i >= 0:
                result[i] += 1
                value -= i
    return result


def what_is_my_sign(day, month):
    formated = 100 * month + day
    ZODIAC = {121: 'Aquarius', 220: 'Pisces', 321: 'Aries', 421: 'Taurus',
              522: 'Gemini', 622: 'Cancer', 723: 'Leo', 823: 'Virgo',
              924: 'Libra', 1024: 'Scorpio', 1123: 'Sagittarius',
              1222: 'Capricorn'}
    while formated not in ZODIAC:
        formated -= 1
    return ZODIAC[formated]
