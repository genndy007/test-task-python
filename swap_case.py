def swap_case(s: str):  # only for english letters
    result = ''

    for unit in s:
        n = ord(unit)
        if 65 <= n <= 90:
            result += chr(n + 32)
        elif 97 <= n <= 122:
            result += chr(n - 32)
        else:
            result += unit

    return result


def swap_case_pythonic(s: str):
    res = ''

    for unit in s:
        res += unit.upper() if unit.islower() else unit.lower()

    return res

def swap_case_very_pythonic(s: str):
    return ''.join([u.upper() if u.islower() else u.lower() for u in s])


t1 = swap_case_very_pythonic('Www.AjaxSystems.com')
print(t1)

t2 = swap_case_very_pythonic('Pythonist 2')
print(t2)