def foo():
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()


def foo1():
    global a
    a = 200
    print(a)


if __name__ == '__main__':
    a = 100
    # foo()
    foo1()
    print(a)
