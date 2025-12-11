# print "honey" 4 times using recurssion
# Head Recursion : first we provide the work and later on fnction call

count = 0


def name():
    global count
    if count == 4:
        return
    print("honey")
    count += 1
    name()


name()
