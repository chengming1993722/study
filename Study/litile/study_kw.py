def f(*args):
    s = 0
    print(args)
    for i in args:
        print(i)
        s+=i
    return s
f(10,20,30)