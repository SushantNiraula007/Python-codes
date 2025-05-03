var1 = 50
var2 = 60
def myfunction():
    "Changes values of global variables"
    globals()['var1'] = globals()['var1'] + 10
    global var2
    var2 = var2 + 20
myfunction()
print("var1:", var1, "var2:", var2)