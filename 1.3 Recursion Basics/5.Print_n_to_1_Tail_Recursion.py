#  N to 1 Tail recursion [Back tracking]


def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)


func(1, 4)
