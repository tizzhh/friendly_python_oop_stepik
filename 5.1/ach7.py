def is_str_num(num: str) -> bool:
    try:
        int(num)
    except ValueError:
        return False
    return True


lst_in = input().split()
print(sum(map(int, filter(is_str_num, lst_in))))
