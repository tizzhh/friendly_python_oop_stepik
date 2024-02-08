try:
    a, b = input().split()
    try:
        res = int(a) + int(b)
    except:
        res = float(a) + float(b)
except:
    res = str(a) + str(b)
finally:
    print(res)
