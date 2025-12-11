# print "honey" 4 times using recurssion
# Head Recursion : first we provide the work and later on fnction call

# Time complexity -> O(N+1) -> O(N)
# Space complexity ->  O(N+1) -> O(N)

count = 0


def name():
    global count
    if count == 4:
        return
    print("honey")
    count += 1
    name()


name()
