lst_in = input().split()

lst_out = []
for elem in lst_in:
    try:
        lst_out.append(int(elem))
    except ValueError:
        try:
            lst_out.append(float(elem))
        except ValueError:
            lst_out.append(elem)
