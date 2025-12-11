# print x, N times -> example x is 15 and N is 3


def func(x, n):
    if n == 0:
        return
    print(f"{x} -> n : {n}")
    func(x, n - 1)


func(15, 4)
