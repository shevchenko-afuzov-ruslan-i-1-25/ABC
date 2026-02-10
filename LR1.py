def f(a,b):
    s = ""
    while a>0:
        if a%b == 10:
            s = "A" + s 
        if a%b == 11:
            s = "B" + s 
        if a%b == 12:
            s = "C" + s 
        if a%b == 13:
            s = "D" + s 
        if a%b == 14:
            s = "E" + s 
        if a%b == 15:
            s = "F" + s 
        if a%b < 10:
            s = str(a%b) + s
        a = a//b
    return s

a = int(input("Введите положительное число для перевода: "))
b = int(input("Введите систему счисления для перевода: "))
print (f(a,b))