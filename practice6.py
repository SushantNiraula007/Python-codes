marks = 50
def myfunction():
    global marks
    marks = marks + 20
    print(marks)

myfunction()
print(marks)