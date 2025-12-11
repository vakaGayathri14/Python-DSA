# print N TO 1 using Head recursion
def func(n):
    if n == 0:
        return
    print(n)
    func(n - 1)


func(5)
