def hex_to_bin(x):
    s = ""
    for i in x:
        if i == "0":
            s = s + "0000" 
        if i == "1":
            s = s + "0001"   
        if i == "2":
            s = s + "0010" 
        if i == "3":
            s = s + "0011"
        if i == "4":
            s = s + "0100" 
        if i == "5":
            s = s + "0101" 
        if i == "6":
            s = s + "0110" 
        if i == "7":
            s = s + "0111" 
        if i == "8":
            s = s + "1000" 
        if i == "9":
            s = s + "1001"   
        if ((i == "A") or (i == "a")):
            s = s + "1010" 
        if ((i == "B") or (i == "b")):
            s = s + "1011"
        if ((i == "C") or (i == "c")):
            s = s + "1100" 
        if ((i == "D") or (i == "d")):
            s = s + "1101" 
        if ((i == "E") or (i == "e")):
            s = s + "1110" 
        if ((i == "F") or (i == "f")):
            s = s + "1111" 
    return s


hex_a = input("Введите число в 16 битном формате IEEE 754:") 
bin_a = hex_to_bin(hex_a)

sign = bin_a[0]
exp_b = bin_a[1:6]
m = bin_a[6:]

if (sign == "0") and (exp_b == "0"*5) and (m == "0" * 10):
    print("Число +0")
    exit()
if (sign == "1") and (exp_b == "0"*5) and (m == "0" * 10):
    print("Число -0")
    exit()
if (sign == "0") and (exp_b == "1"*5) and (m == "0" * 10):
    print("Число +∞")
    exit()
if (sign == "1") and (exp_b == "1"*5) and (m == "0" * 10):
    print("Число -∞")
    exit()

if (exp_b == "1"*5):
    print("не считается числом (NAN)")

if exp_b == "0"*5:
    F = ((-1)**int(sign,2)) * (2**(int(exp_b,2) - 2**(5-1) + 2)) * (int(m,2)/(2**10))
    print("Ваше число в десятичной форме:",f'{F:.170f}')
    exit()

F = ((-1)**int(sign,2)) * (2**(int(exp_b,2) - 2**(5-1) + 1)) * (1 + int(m,2)/(2**10))
print("Ваше число в десятичной форме:",f'{F:.160f}')
