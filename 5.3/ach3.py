def input_int_numbers():
    inp = input().split()
    return tuple(int(x) for x in inp)


while True:
    try:
        res = input_int_numbers()
    except:
        ...
    else:
        break


print(*res)
