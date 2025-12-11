# Tail recursion : First we call the function later on the work has to be done

# print name 4 times

# Time complexity -> O(N+1) -> O(N)
# Space complexity ->  O(N+1) -> O(N)

count = 0


def name():
    global count
    if count == 4:
        return
    count += 1
    name()
    print("honey")


name()
