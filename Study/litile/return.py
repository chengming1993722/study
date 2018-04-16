def A():
    a = 1
    b = 2
    return [a,
            b]

if __name__ == '__main__':
    C = A()
    print(C)
    print(type(C))