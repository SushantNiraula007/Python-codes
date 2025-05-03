def yourfunction():
    a = 5
    b = 6
    def myfunction():
        #nonlocal a
        #nonlocal b
        a = 10
        b = 20
        print("Variable a:", a)
        print("Variable b:", b)
        return a+b
    print(myfunction())
    print("Variable a:", a)
    print("Variable b:", b)
yourfunction()
